import tkinter
import cv2
import PIL.Image,	PIL.ImageTk
import time
import os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# create folder directory to save images
folder = r"/trippy/"
cwd = os.getcwd()
path = cwd+folder
if not os.path.exists(path):
    os.makedirs(path)

# create a dictionary for the filters
fil = ['color', 'gray', 'seppia','stileretro','sharp', 'vintage_classic', 'threshold', 'polaroid', 'old_film_filter', 'take a video!']
filter_dic = {}
def select_filter(filter, status):
    # change required filter to true
    filter_dic = {x:False for x in fil}
    if filter in filter_dic:
        assert type(status) == bool
        filter_dic[filter] = status
    return filter_dic

# Begin the app
class	App:
    def	__init__(self,	window,	window_title, video_source=0):
        self.window	= window
        self.window.title(window_title)
        self.video_source =	video_source
        self.vid = MyVideoCapture(self.video_source)

        # initialize the filters
        self.all_filters = select_filter('color', True)
        self.frame_delta_plus = None

        # Labels
        label1 = tkinter.Label(window,text="Filters")
        label1.grid(row=0,column=13, columnspan=5)

        label2 = tkinter.Label(window, text="Saving")
        label2.grid(row=8,column=13, columnspan=5)

        #	Create	a	canvas	that	can	fit	the	above	video	source	size
        self.canvas	= tkinter.Canvas(window, width = self.vid.width, height	= self.vid.height)
        self.canvas.grid(row=0, column=1, rowspan=9, columnspan=5)

        #	Button	that	lets	the	user	take	a	snapshot
        self.b_snap=tkinter.Button(window, text="Snapshot", width=50,	command=self.snapshot)
        self.b_snap.grid(row=12, column=3, rowspan=7)

        # Button for applying the other filters!
        self.b1 = tkinter.Button(window, text="Seppia classic", width=15, command=self.seppia_filter)
        self.b1.grid(row=1, column=13)

        self.b2 = tkinter.Button(window, text="Vintage Classic", width=15, command=self.vintage_classic_filter)
        self.b2.grid(row=1, column=17)

        self.b3 = tkinter.Button(window, text="stile retrò", width=15,  command=self.stileretro_filter)
        self.b3.grid(row=3, column=13)

        self.b3_2 = tkinter.Button(window,text="Polaroid", width = 10, command=self.polaroid_filter)
        self.b3_2.grid(row=4, column=13)

        self.b4 = tkinter.Button(window, text="Threshold", width=15, command=self.threshold_filter)
        self.b4.grid(row=3, column=17)

        # note, sobel filters use the same button, multiple clicks
        self.b5 = tkinter.Button(window, text="SHARP", width=15, command=self.sharp_filter)
        self.b5.grid(row=5, column=13)

        #self.b6 = tkinter.Button(window, text="old_film_filter", width = 15, command = self.old_film_filter)
        #self.b6.grid(row=5, column= 17)

        self.b7 = tkinter.Button(window, text="Gray", width=15, command=self.gray_filter)
        self.b7.grid(row=7, column=13)

        self.b8 = tkinter.Button(window, text="Color/No Filter", width=15, command=self.no_filter)
        self.b8.grid(row=7, column=17)

        self.b9 = tkinter.Button(window, text="take a video!",command=self.take_video)
        self.b9.grid(row=9, rowspan=2, column = 13, columnspan=4)

        self.b10= tkinter.Button(window, text="Close Program",  command=window.destroy)
        self.b10.grid(row=9, rowspan=2, column=17, columnspan=2)

        #	After	it	is	called	once,	the	update	method	will	be	automatically	called	every loop
        self.delay = 15
        self.update()
        self.window.mainloop()

    def	snapshot(self):
        cv2.imwrite(path+r"frame-"+time.strftime("%d-%m-%Y-%H-%M-%S")+'.jpg', self.frame)



    def	update(self):
        # print('update is working')
        ret,frame, frame1 = self.vid.get_frame()

        def take_video(frame):
            vid_cod = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
            output = cv2.VideoWriter("cam_video.avi", vid_cod, 20.0, (640, 480))
            # output = cv2.VideoWriter('output.avi', -1, 20.0, (640, 480))
            while True:
                # Capture each frame of webcam video
                # ret, frame = vid_capture.read()
                output.write(frame)
                # Close and break the loop after pressing "x" key
                if cv2.waitKey(1) & 0XFF == ord('x'):
                    break

        # return output

        def gray_filter(frame):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return gray
        def seppia_filter(frame):
            array = np.array(frame)
            seppiaMatrix = np.array([[0.500, 0.770, 0.200], [0.422, 0.616, 0.168], [0.092, 0.598, 0.120]])
            filter = cv2.transform(array, seppiaMatrix)
            # Check wich entries have a value greather than 255 and set it to 255
            filter[np.where(filter > 255)] = 255
            output_pil: Image
            output_pil = Image.fromarray(filter)
            output_np = np.array(output_pil)
            output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)
            return output_cv
        def stileretro_filter(frame):
            frame:Image
            rows, cols = frame.shape[:2]
            # Create a Gaussian filter
            kernel_x = cv2.getGaussianKernel(cols, 400)
            kernel_y = cv2.getGaussianKernel(rows, 400)
            kernel = kernel_y * kernel_x.T
            filter = 255 * kernel / np.linalg.norm(kernel)
            vintage_im = np.copy(frame)
            # for each channel in the input image, we will apply the above filter
            for i in range(3):
                vintage_im[:, :, i] = vintage_im[:, :, i] * filter

            array = np.array(vintage_im)
            seppiaMatrix = np.array([[0.393, 0.769, 0.189],[0.349, 0.686, 0.168],[0.272, 0.534, 0.131]])
            filter = cv2.transform(array, seppiaMatrix)
            # Check wich entries have a value greather than 255 and set it to 255
            filter[np.where(filter > 255)] = 255
            output_pil: Image
            output_pil = Image.fromarray(filter)
            output_np = np.array(output_pil)
            output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)
            ### applica sherpening
            Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            output_sherpen = cv2.filter2D(output_cv, -1, Kernel)
            ## applica maschera scratch
            mask = cv2.imread('foto/cartastropicciata.jpg')
            mask_resized = cv2.resize(mask, (output_sherpen.shape[1], output_sherpen.shape[0]))
            dst = cv2.addWeighted(output_sherpen, 0.7, mask_resized, 0.5, 0)
            return dst
        def sharp_filter(frame):
            frame : Image
            Kernel = np.array([[-1, -1, -1],[-1, 9, -1], [-1, -1, -1]])
            input = cv2.filter2D(frame, -1, Kernel)
            array = np.array(input)
            vissutoMatrix = np.array([[0.300, 0.300, 0.300],
                                     [0.270, 0.300, 0.270],
                                     [0.300, 0.255, 0.153]
                                     ])
            filter = cv2.transform(array, vissutoMatrix)
            # Check wich entries have a value greather than 255 and set it to 255
            filter[np.where(filter > 255)] = 255
            output_pil: Image
            output_pil = Image.fromarray(filter)
            output_np = np.array(output_pil)
            output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)
            return output_cv
        def vintage_classic_filter(frame):
            frame : Image
            rows, cols = frame.shape[:2]
            # Create a Gaussian filter
            kernel_x = cv2.getGaussianKernel(cols, 400)
            kernel_y = cv2.getGaussianKernel(rows, 400)
            kernel = kernel_y * kernel_x.T
            filter = 255 * kernel / np.linalg.norm(kernel)
            vintage_im = np.copy(frame)
            # for each channel in the input image, we will apply the above filter
            for i in range(3):
                vintage_im[:, :, i] = vintage_im[:, :, i] * filter

            array = np.array(vintage_im)
            seppiaMatrix = np.array([[0.393, 0.769, 0.189],[0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])
            filter = cv2.transform(array, seppiaMatrix)
            # Check wich entries have a value greather than 255 and set it to 255
            filter[np.where(filter > 255)] = 255
            output_pil: Image
            output_pil = Image.fromarray(filter)
            output_np = np.array(output_pil)
            output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)
            return output_cv
        def threshold_filter(frame):
            trash = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            return trash
        def polaroid_filter(frame):
            blur = cv2.GaussianBlur(frame, (5, 5), cv2.BORDER_DEFAULT)
            red_img = np.full((682, 512, 3), (0, 0, 220), np.uint8)
            mask_resized = cv2.resize(red_img, (frame.shape[1], frame.shape[0]))
            fused_img = cv2.addWeighted(frame, 0.8, mask_resized, 0.2, 0)
            WHITE = [255, 255, 255]
            black_border_img = cv2.copyMakeBorder(fused_img, 60, 60, 20, 20, cv2.BORDER_CONSTANT, value=WHITE)
            return black_border_img
        def old_film_filter(frame):
            mask_filter = cv2.VideoCapture('video/OldFilm_lungo.mp4')
            cap = frame
            while cap.isOpened():
                ret, frame2 = cap.read()
                ret1, frame1 = mask_filter.read()
                if ret == True and ret1 == True:
                    h, w, c = frame2.shape
                    h1, w1, c1 = frame1.shape
                    if h != h1 or w != w1:
                        frame2 = cv2.resize(frame2, (w1, h1))

                    both = cv2.addWeighted(frame2, 0.9, frame1, 0.7, 0)

                    cv2.imshow('Frame', both)

                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break
                else:
                    break

            return cap


        if self.all_filters['color']:
            pass
        elif self.all_filters['gray']:
            frame = gray_filter(frame)
        elif self.all_filters['seppia']:
            frame = seppia_filter(frame)
        elif self.all_filters['stileretro']:
            frame = stileretro_filter(frame)
            # self.frame_delta = frame
        elif self.all_filters['sharp']:
            frame = sharp_filter(frame)
        elif self.all_filters['vintage_classic']:
            frame = vintage_classic_filter(frame)
        elif self.all_filters['threshold']:
            frame = threshold_filter(frame)
        elif self.all_filters['polaroid']:
            frame = polaroid_filter(frame)
        elif self.all_filters['take a video!']:
            frame = take_video(frame)
        #elif self.all_filters['old_film_filter']:
           # frame = old_film_filter(frame)
        # If there's a frame, create an image to display on the canvas
        if	ret:
            self.frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.frame))
            self.canvas.create_image(0,0,image=self.photo,anchor=tkinter.NW)
        self.window.after(self.delay,self.update)

        # update frames for snapshot
        self.frame = frame
    # all filters
    def gray_filter(self):
        self.all_filters = select_filter('gray', True)
    def delta_filter_plus(self):
        self.frame_delta_plus = None
        self.all_filters = select_filter('delta_plus', True)
    def seppia_filter(self):
        self.all_filters = select_filter('seppia', True)
    def stileretro_filter(self):
        self.all_filters = select_filter('stileretro', True)
    def vintage_classic_filter(self):
        self.all_filters = select_filter('vintage_classic', True)
    def threshold_filter(self):
        self.all_filters = select_filter('threshold', True)
    def sharp_filter(self):
        self.all_filters = select_filter('sharp', True)
    def no_filter(self):
        self.all_filters = select_filter('color', True)
    #def old_film_filter(self):
        #self.all_filters = select_filter('old_film_filter', True)
    def polaroid_filter(self):
        self.all_filters = select_filter('polaroid', True)
    def take_video(self):
        self.all_filters = select_filter('take a video!', True)

class	MyVideoCapture:
    def	__init__(self,video_source=0):
        #	Open	the	video	source
        self.vid=cv2.VideoCapture(video_source)
        if	not	self.vid.isOpened():
            raiseValueError("Unable	to open	video source", video_source)

        #	Get	video	source	width	and	height
        self.width	= self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height	= self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        global_frame1 = None
        self.frame1 = global_frame1

    def	get_frame(self):
        if	self.vid.isOpened():
            ret, frame = self.vid.read()
            if self.frame1 is None:
                self.frame1= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if ret:
                return (ret, frame, self.frame1)
            else:
                return (ret, None)
        else:
            return	(ret, None)

    #	clear the video when the object is destroyed
    def	__del__(self):
        if	self.vid.isOpened():
            self.vid.release()
#	Create	a	window	and	pass	it	to	the	Application	object
App(tkinter.Tk(), 'Vintage Cam')