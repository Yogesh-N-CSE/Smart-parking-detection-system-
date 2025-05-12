Here’s a concise **overview** of the smart parking detection system code built for **Google Colab**:

---

### **Overview: Smart Parking Detection in Colab**

This Python program uses **OpenCV** to detect whether predefined parking spots are **occupied or free** based on an uploaded **video** file. It processes the **first frame** of the video and visually marks the parking status.

---

### **Key Components:**

1. **Dependencies Installation**

   * Installs `opencv-python-headless` (a Colab-friendly version of OpenCV).

2. **Video Upload**

   * Allows the user to upload a parking lot video from their local device via `google.colab.files.upload()`.

3. **Parking Spot Setup**

   * Defines the coordinates of parking spots manually as `(x, y, width, height)` rectangles.

4. **Occupancy Detection**

   * Converts each spot region to grayscale.
   * Applies Gaussian blur and binary thresholding.
   * Counts non-zero pixels to determine if a car is present (based on pixel activity).
   * A threshold value is used to distinguish between "free" and "occupied".

5. **Visualization**

   * Draws rectangles around each parking spot:

     * **Red** for **occupied**
     * **Green** for **free**
   * Displays the annotated frame using `cv2_imshow`.

---

### **Use Case:**

* Helpful for creating basic smart parking prototypes.
* Works well for fixed camera angles and static spot coordinates.




