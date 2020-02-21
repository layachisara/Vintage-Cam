import tkinter
import cv2
import PIL.Image,	PIL.ImageTk
import time
import os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageGrab

# create folder directory to save images
folder = r"/Vintage Cam/"
cwd = os.getcwd()
path = cwd+folder
if not os.path.exists(path):
    os.makedirs(path)

# create a dictionary for the filters
fil = ['Classic Seppia', 'Dark Vintage', 'Dirty Gray', 'Dreaming On', 'Polaroid', 'Sweet Dusty', 'Stile Retro']
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
    def	__init__(self,	window,	window_title,	video_source=0):
        self.window	= window
        self.window.title(window_title)
        self.video_source =	video_source
        self.vid = MyVideoCapture(self.video_source)

        # initialize the filters
        self.all_filters = select_filter('color', True)
        self.frame_delta_plus = None

        # Creazione label applicazione
        label1 = tkinter.Label(window, text="Filtri Immagini")
        label1.grid(row=0, column=13, columnspan=5)

        #label2 = tkinter.Label(window, text="Filtri Video")
        #label2.grid(row=9, column=13, columnspan=5)

        label3 = tkinter.Label(window, text="Salvataggio")
        label3.grid(row=20, column=13, columnspan=5)

        # Comando per creare spazio in cui caricare immagine acquisita da Cam
        self.canvas	= tkinter.Canvas(window, width = 1000, height=700)
        self.canvas.grid(row=0, column=1, rowspan=15, columnspan=5)

        #self.canvas = tkinter.Canvas(window, width=600, height=400)
        #self.canvas.grid(row=0, column=1, rowspan=15, columnspan=5)

        # Crea il bottone per fare uno Snapshot
        self.b_snap=tkinter.Button(window, text="Snapshot", width=100, command=self.snapshot)
        self.b_snap.grid(row=28, column=3, rowspan=20)

        # Button for applying the other filters!
        self.b1 = tkinter.Button(window, text="Classic Seppia", width=15, command=self.seppia_filter)
        self.b1.grid(row=1, column=13)

        self.b2 = tkinter.Button(window, text="Dark Vintage", width=15, command=self.dark_vintage)
        self.b2.grid(row=1, column=17)

        self.b3 = tkinter.Button(window, text="Dirty Gray", width=15, command=self.dirty_gray)
        self.b3.grid(row=3, column=13)

        self.b4 = tkinter.Button(window, text="Dreaming On", width=15, command=self.dreaming_on)
        self.b4.grid(row=3, column=17)

        self.b5 = tkinter.Button(window, text="Polaroid", width=15, command=self.polaroid_filter)
        self.b5.grid(row=5, column=13)

        self.b6 = tkinter.Button(window, text="Sweet Dusty", width=15, command=self.sweet_dusty)
        self.b6.grid(row=5, column=17)

        self.b7 = tkinter.Button(window, text="Stile Retro", width=15, command=self.stile_retro)
        self.b7.grid(row=7, column=13)

        #self.b1 = tkinter.Button(window, text="Classic Seppia", width=15, command=self.seppia_filter)
        #self.b1.grid(row=10, column=13)

        #self.b2 = tkinter.Button(window, text="Dark Vintage", width=15, command=self.dark_vintage)
        #self.b2.grid(row=10, column=17)

        #self.b3 = tkinter.Button(window, text="Dirty Gray", width=15, command=self.dirty_gray)
        #self.b3.grid(row=12, column=13)

        #self.b4 = tkinter.Button(window, text="Dreaming On", width=15, command=self.dreaming_on)
        #self.b4.grid(row=12, column=17)

        #self.b5 = tkinter.Button(window, text="Polaroid", width=15, command=self.polaroid_filter)
        #self.b5.grid(row=14, column=13)

        #self.b6 = tkinter.Button(window, text="Sweet Dusty", width=15, command=self.sweet_dusty)
        #self.b6.grid(row=14, column=17)

        #self.b7 = tkinter.Button(window, text="Stile Retro", width=15, command=self.stile_retro)
        #self.b7.grid(row=16, column=13)

        #self.b8 = tkinter.Button(window, text="Old Film", width=15)  # , command=self.threshold_filter)
        #self.b8.grid(row=16, column=17)

        #self.b9 = tkinter.Button(window, text="Old Tv", width=15)  # , command=self.threshold_filter)
        #self.b9.grid(row=18, column=13)

        self.b9 = tkinter.Button(window, text="Snapshot!", command=self.snapshot)
        self.b9.grid(row=26, rowspan=2, column = 13, columnspan=4)

        self.b10= tkinter.Button(window, text="Chiudi Vintage Cam", command=window.destroy)
        self.b10.grid(row=26, rowspan=2, column=17, columnspan=4)

        #	After	it	is	called	once,	the	update	method	will	be	automatically	called	every loop
        self.delay = 15
        self.update()
        self.window.mainloop()

    def snapshot(self):
        cv2.imwrite(path + r"frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + '.jpg', self.frame)

    def update(self):
        # print('update is working')
        ret, frame, frame1 = self.vid.get_frame()

        def seppia_filter(frame):
           array = np.array(frame)
           seppiaMatrix = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])
           filter = cv2.transform(array, seppiaMatrix)
           # Check wich entries have a value greather than 255 and set it to 255
           filter[np.where(filter > 255)] = 255

           # Create an image from the array
           output: Image
           output = Image.fromarray(filter)

           # conversion from Pil to cv
           output_np = np.array(output)
           output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)

           # add texture
           mask = cv2.imread('Texture/blu-texture.jpg')
           mask_resized = cv2.resize(mask, (output_cv.shape[1], output_cv.shape[0]))
           output = cv2.addWeighted(output_cv, 0.7, mask_resized, 0.1, 0)
           return output


        def dark_vintage(frame):

            # apply dark vintage filter
            # Gaussian filter
            rows, cols = frame.shape[:2]
            kernel_x = cv2.getGaussianKernel(cols, 170)
            kernel_y = cv2.getGaussianKernel(rows, 170)
            kernel = kernel_y * kernel_x.T
            filter = 255 * kernel / np.linalg.norm(kernel)
            vintage_im = np.copy(frame)
            # for each channel in the input image, we will apply the above filter
            for i in range(3):
                vintage_im[:, :, i] = vintage_im[:, :, i] * filter

            # add texture
            mask = cv2.imread('Texture/blu-texture.jpg')
            mask_resized = cv2.resize(mask, (vintage_im.shape[1], vintage_im.shape[0]))
            dst = cv2.addWeighted(vintage_im, 0.7, mask_resized, 0.3, 0)

            # covert to gray
            gray_im = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
            return gray_im

        def dirty_gray(frame):
            # gray filter
            output_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # shrapening filter
            Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            output_sharpen = cv2.filter2D(output_gray, -1, Kernel)
            return output_sharpen

        def dreaming_on(frame):
            # add texture
            mask = cv2.imread('Texture/texture-dream.jpg')
            mask_resized = cv2.resize(mask, (frame.shape[1], frame.shape[0]))
            output1 = cv2.addWeighted(frame, 0.7, mask_resized, 0.6, 0)

            # add texture
            mask = cv2.imread('Texture/blu-texture.jpg')
            mask_resized = cv2.resize(mask, (output1.shape[1], output1.shape[0]))
            output2 = cv2.addWeighted(output1, 0.7, mask_resized, 0.2, 0)
            return output2

        def polaroid_filter(frame):
            # add BLURRING: image blurring is achieved by convolving the image with a low-pass filter kernel.

            Kernel = np.ones((4, 4), np.float32) / 16
            blur_img = cv2.filter2D(frame, -1, Kernel)

            mask = cv2.imread('Texture/polaroid-texture.jpg')
            mask_resized = cv2.resize(mask, (blur_img.shape[1], blur_img.shape[0]))
            out = cv2.addWeighted(blur_img, 0.7, mask_resized, 0.5, 0)

            # create an image with a single color (red)
            red_img = np.full((682, 512, 3), (0, 0, 150), np.uint8)
            mask_resized = cv2.resize(red_img, (out.shape[1], out.shape[0]))

            # add the filter  with a weight factor of 20% to the target image
            fused_img = cv2.addWeighted(out, 0.8, mask_resized, 0.2, 0)
            WHITE = [255, 255, 255]
            white_border_img = cv2.copyMakeBorder(fused_img, 60, 60, 20, 20, cv2.BORDER_CONSTANT, value=WHITE)

            # add text
            position = (200, 650)
            cv2.putText(
                white_border_img,  # numpy array on which text is written
                "Vintage Cam",  # text
                position,  # position at which writing has to start
                cv2.FONT_HERSHEY_SIMPLEX,  # font family
                1,  # font size
                (0, 0, 0, 0),  # font color
                3)  # font stroke
            return white_border_img

        def sweet_dusty(frame):
            # add blur
            kernel = np.ones((4, 4), np.float32) / 16
            blur_img = cv2.filter2D(frame, -1, kernel)

            # add texture
            mask = cv2.imread('Texture/texture-dust.jpg')
            mask_resized = cv2.resize(mask, (blur_img.shape[1], blur_img.shape[0]))
            output = cv2.addWeighted(blur_img, 0.7, mask_resized, 0.2, 0)
            return output


        def stile_retro(frame):
            # apply seppia filter
            array = np.array(frame)
            seppiaMatrix = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])
            filter = cv2.transform(array, seppiaMatrix)
            # Check wich entries have a value greather than 255 and set it to 255
            filter[np.where(filter > 255)] = 255
            output_pil: Image
            output_pil = Image.fromarray(filter)
            output_np = np.array(output_pil)
            output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR)

            # apply sherpening
            Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            output_sherpen = cv2.filter2D(output_cv, -1, Kernel)

            return output_sherpen

        if self.all_filters['Classic Seppia']:
            frame = seppia_filter(frame)
        elif self.all_filters['Dark Vintage']:
            frame = dark_vintage(frame)
        elif self.all_filters['Dirty Gray']:
            frame = dirty_gray(frame)
        elif self.all_filters['Dreaming On']:
            frame = dreaming_on(frame)
        elif self.all_filters['Polaroid']:
            frame = polaroid_filter(frame)
        elif self.all_filters['Sweet Dusty']:
            frame = sweet_dusty(frame)
        elif self.all_filters['Stile Retro']:
            frame = stile_retro(frame)

        # If there's a frame, create an image to display on the canvas
        if ret:
            self.frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.window.after(self.delay, self.update)

        # update frames for snapshot
        self.frame = frame
        # all filters

    def seppia_filter(self):
        self.all_filters = select_filter('Classic Seppia', True)

    def dark_vintage(self):
        self.all_filters = select_filter('Dark Vintage', True)

    def dirty_gray(self):
        self.all_filters = select_filter('Dirty Gray', True)

    def dreaming_on(self):
        self.all_filters = select_filter('Dreaming On', True)

    def polaroid_filter(self):
        self.all_filters = select_filter('Polaroid', True)

    def sweet_dusty(self):
        self.all_filters = select_filter('Sweet Dusty', True)

    def stile_retro(self):
        self.all_filters = select_filter('Stile Retro', True)


class MyVideoCapture:
        def __init__(self, video_source=0):
            #	Open	the	video	source
            self.vid = cv2.VideoCapture(video_source)
            if not self.vid.isOpened():
                raiseValueError("Unable	to open	video source", video_source)

            #	Get	video	source	width	and	height
            self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
            global_frame1 = None
            self.frame1 = global_frame1

        def get_frame(self):
            if self.vid.isOpened():
                ret, frame = self.vid.read()
                if self.frame1 is None:
                    self.frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if ret:
                    return (ret, frame, self.frame1)
                else:
                    return (ret, None)
            else:
                return (ret, None)


        # clear the video when the object is destroyed
        def __del__(self):
            if self.vid.isOpened():
               self.vid.release()




            # Create a window and pass it to the	Application	object
App(tkinter.Tk(), 'Vintage Cam')

