from photo_editor_view1 import PhotoView
from photo_editor_model1 import PhotoModel

def main():
    
    model = PhotoModel
    photo=PhotoView(model)
    #img_path = photo.img_path()
    #model.open_img(img_path)
    photo.GUI()
if __name__ == "__main__":
    main()