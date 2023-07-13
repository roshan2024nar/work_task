import cv2
import numpy as np

def detect_and_inpaint_number_plate(image_path):
    
    """
    Detects number plates in an image and inpaints them to hide the numbers.

    Args:
        image_path (str): The path to the input image file.

    Returns:
        None
        
    Examples:
            image_path = "carimage.jpg"
            detect_and_inpaint_number_plate(image_path)

    """
    
    image = cv2.imread(image_path)

    cv2.imshow("Before", image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    number_plate_cascade = cv2.CascadeClassifier("cascade\haarcascade_russian_plate_number.xml")


    number_plates = number_plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    mask = np.zeros(gray.shape, dtype=np.uint8)


    for (x, y, w, h) in number_plates:
        inpaint_roi = image[y:y+h, x:x+w]
        mask_roi = mask[y:y+h, x:x+w]
        inpainted_roi = cv2.inpaint(inpaint_roi, mask_roi, 3, cv2.INPAINT_TELEA)
        image[y:y+h, x:x+w] = inpainted_roi


        image[y:y+h, x:x+w] = 255


    cv2.imshow("After", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_and_inpaint_number_plate("images\carimage.jpg")