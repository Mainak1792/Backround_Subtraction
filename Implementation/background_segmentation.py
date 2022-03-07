import numpy as np
import cv2

#define the model(pdf)
def norm_pdf(x, mean, s):
    return (1 / (np.sqrt(2 * np.pi) * s)) * (np.exp(-0.5 * (((x - mean) / s) ** 2)))

def normo(omega):
    s = np.sum(omega, axis=0)
    omega = omega / s
    return omega

#defining the sort function
def sort(x,index):
    x = np.take_along_axis(x, index, axis=0)
    return x


class background_segmentation():
    def __init__(self, cap, alpha, T):
        self.cap = cap
        self.alpha = alpha
        self.T = T

        _, frame = self.cap.read()
        #convert RGB frames to grayscale
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Extract height and width of the frame
        self.height, self.width = frame.shape
        
        #initialise sample mean matrix
        self.mean = np.zeros([3, self.height, self.width], np.float64)
        self.mean[1, :, :] = frame
        
        #initialise sample covariance matrix
        self.var = np.zeros([3, self.height, self.width], np.float64)
        self.var[:, :, :] = 5
        
        #initialise sample weight matrix
        self.omega = np.zeros([3, self.height, self.width], np.float64)
        self.omega[0, :, :], self.omega[1, :, :], self.omega[2, :, :] = 0, 0, 1
        
        #initailise weight/ sigma matrix to sort K gaussians
        self.omega_by_s = np.zeros([3, self.height, self.width], np.float64)
        
        #initialise background matrix
        self.background = np.zeros([self.height, self.width], np.uint8)
        
        # initialise s matrix: standard_deviation 
        # initialise v matrix: 2.5 * standard_deviation 
        # initialise Compare_val matrix: Difference of pixel intensity between current frame and mean value
        self.s = np.zeros([3,self.height,self.width], np.float64)
        self.v = np.zeros([3, self.height, self.width], np.float64)
        self.compare_val = np.zeros([3, self.height, self.width], np.float64)
        
        #update negative_variance
        #update standard_deviation and 2.5 * standard deviation
        for i in range(3):
            self.var[i][np.where(self.var[i] < 1)] = 5
            self.s[i] = np.sqrt(self.var[i]) 
            self.v[i]= 2.5 * self.s[i]
    
    def update_parameter(self):
        while self.cap.isOpened():
            _, frame = self.cap.read()
            #convert RGB frmes to grayscale
            fg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            gauss_match = []
            gauss_not_match = []

            # converting data type of fg so that different operation with it can be performed
            fg = fg.astype(np.float64)
            #Update(xi-uj)
            #Either_It_matches_2.5(standard_deviation)
            #Or_it_doesnot_2.5(standard_deviation)
            
            for i in range(3):
                self.compare_val[i] = cv2.absdiff(fg, self.mean[i])
                
                # finding self.omega_by_s for ordering of the gaussian
                self.omega_by_s[i] = self.omega[i] / self.s[i]
                
                #update indices where there is at least one gaussian match
                gauss_fit = np.where(self.compare_val[i] <= self.v[i])
                gauss_match.append(gauss_fit)
            
                #update indices where there is no gaussian match
                gauss_not_fit = np.where(self.compare_val[i] > self.v[i])
                gauss_not_match.append(gauss_not_fit)
                
            # Consider_the_indices>threshold(Weight_or_combination_of_Weights)
            # Consider_the_indices<threshold
            fore_index1 = np.where(self.omega[2] > self.T)
            fore_index2 = np.where(((self.omega[2] + self.omega[1]) > self.T) & (self.omega[2] < self.T))
            
            y = gauss_match[2]
            # updating indices where line 104 satisfies (matching definition)
            temp = np.zeros([self.height, self.width])
            temp[fore_index1] = 1
            temp[y] = temp[y] + 1
            index3 = np.where(temp == 2)

            # updating indices where line 105 satisfies (matching definition)
            temp = np.zeros([self.height, self.width])
            temp[fore_index2] = 1
            index = np.where((self.compare_val[2] <= self.v[2]) | (self.compare_val[1] <= self.v[1]))
            temp[index] = temp[index] + 1
            index2 = np.where(temp == 2)
                
            self.not_match_index = np.zeros([3, self.height, self.width])
            self.match_index = np.zeros([self.height,self.width])
            
            self.match_index[gauss_match[0]] = 1
            self.match_index[gauss_match[1]] = 1
            self.match_index[gauss_match[2]] = 1
    
            self.not_match_index = np.where(self.match_index == 0)
            
            # Update_parameters for the matched  Gaussians
            # update mean, covariance and weights
            # Rho : [0,1], input Learning Rate

            for j in range(3):
                # update var and mean value of the matched indices of all three gaussians
                rho = self.alpha * norm_pdf(fg[gauss_match[j]], self.mean[j][gauss_match[j]], self.s[j][gauss_match[j]])
                constant = rho * ((fg[gauss_match[j]] - self.mean[j][gauss_match[j]]) ** 2)
                self.mean[j][gauss_match[j]] = (1 - rho) * self.mean[j][gauss_match[j]] + rho * fg[gauss_match[j]]
                self.var[j][gauss_match[j]] = (1 - rho) * self.var[j][gauss_match[j]] + constant
                self.omega[j][gauss_match[j]] = (1 - self.alpha) * self.omega[j][gauss_match[j]] + self.alpha
                self.omega[j][gauss_not_match[j]] = (1 - self.alpha) * self.omega[j][gauss_not_match[j]]
           
            # update least probable gaussian for those pixel values which do not match any of the gaussian
            self.mean[0][self.not_match_index] = fg[self.not_match_index]
            self.var[0][self.not_match_index] = 500
            self.omega[0][self.not_match_index] = 0.1
        
            # normalise omega
            self.omega=normo(self.omega) #normalise omega
            
            
            #finding omega by sigma for ordering of the gaussian
            for i in range(2):
                self.omega_by_s[i] = self.omega[i] / self.s[i]
            
            # getting index order for sorting self.omega by s
            index = np.argsort(self.omega_by_s, axis=0)

            # from that index(line 139) sorting self.mean,self.var and self.omega
            # sorting the mean, variance and Omega
            self.mean=  sort(self.mean, index)
            self.var= sort(self.var , index)
            self.omega= sort(self.omega, index)

            # converting data type of fg so that we can use it to perform operations for displaying the image
            fg = fg.astype(np.uint8)

            # getting background from the index2 and index3
            self.background[index2] = fg[index2]
            self.background[index3] = fg[index3]
            
            cv2.imshow('original',fg)
        
            # background and foreground video
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(fg,
                    "Mainak,Priyanka,Deepak",
                    (20, 20),
                    font, 0.4,
                    (255, 0, 0),
                    2)
            
            cv2.imshow('Background', self.background)
            cv2.imshow('foreground',cv2.absdiff(fg,self.background))
            cv2.imshow('original',fg)
            if cv2.waitKey(1) & 0xFF == 27:
                    break
        self.cap.release()
        cv2.destroyAllWindows()

    