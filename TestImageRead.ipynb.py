#!/usr/bin/env python
# coding: utf-8

# ### The following takes a one page document saved as a .png, and converts to text.

# In[19]:


import os
get_ipython().system('ls #will print files in your current working directory')
os.getcwd() #will print the path to your current working directory.  
            #This is where your images will be saved
            #I created a folder in here for pdfs, and called it PDFs


# In[20]:


pip install opencv-python


# In[21]:


import cv2
image = cv2.imread("/Users/nikhiljain/Downloads/RTI_test_image.png")


# In[22]:


import matplotlib.pyplot as plt
plt.imshow(image)


# In[23]:


get_ipython().system('pip install pytesseract')
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


# In[24]:


text = pytesseract.image_to_string(Image.open("/Users/nikhiljain/Downloads/RTI_test_image.png"))
text_original = str(text)
print(text_original)


# ### Now, we'd like to be able to take the .pdfs directly from the website.  We first need to convert them to an image file, then process them.

# ###### 1) Download .pdf from the website.  We can create a loop to do this for all documents.

# In[25]:


from urllib.request import urlretrieve


# In[26]:


get_ipython().system('pip install pdf2image')
from pathlib import Path
import requests
filename = Path('/Users/nikhiljain/Downloads/RTI_Sh_S_Rahul.pdf') #file path + file name
url = "https://mea.gov.in/Images/attach/RTI_Sh_S_Rahul.pdf" #url for the pdf to be downloaded
response = requests.get(url)
filename.write_bytes(response.content)


# ##### 2) Convert the .pdf to .jpg

# In[ ]:


conda install -c conda-forge poppler


# In[ ]:


from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pdf2image import convert_from_path


# In[ ]:


get_ipython().system('cd Images')


# In[ ]:


get_ipython().system('ls')


# In[ ]:


image = convert_from_path('/Users/nikhiljain/Downloads/RTI_Sh_S_Rahul.pdf', dpi=500, ) #can add commands to skip pages #this creates each page as an element in an array
for (i,page) in enumerate(image):
    image[i].save('RTI_Sh_S_Rahul.pdf'+ str(i) +'.jpg', 'JPEG') #save each page seperately


# In[ ]:


#Check to be sure that files saved
get_ipython().system('ls')


# #### Now convert the images to text.

# In[ ]:


for (i,page) in enumerate(image):
    text = pytesseract.image_to_string(Image.open('/Users/nikhiljain/RTI_Sh_S_Rahul.pdf'+ str(i) +'.jpg'))
    text_original = str(text)
    print(text_original)


# In[ ]:




