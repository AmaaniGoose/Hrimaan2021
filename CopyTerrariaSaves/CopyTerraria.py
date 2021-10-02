#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shutil
import os
import time
import stat


# In[2]:


src=''


# In[3]:


src_files = os.listdir(src)
dest=''
print(src_files)


# In[4]:


for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)
        


# In[5]:


dest_files=os.listdir(dest)
for file_name in dest_files:
    full_file_name = os.path.join(dest, file_name)
    fileStatsObj = os.stat ( full_file_name )
    modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
    print(f"File name {file_name} Last Modified Time : {modificationTime}")
print("Task completed successfully")


# In[ ]:




