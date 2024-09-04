


f = open('fileone.txt','w+')
f.write('one file')
f.close()

f = open('filetwo.txt','w+')
f.write('two file')
f.close()

import zipfile

# how to zip
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()

# how to extract from zip file

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_content')


##############################################

# to zip the folder from shell unitilities
import shutil

dir_to_zip = '/Users/indraneelsarode/Desktop/Python-basics-to-advance/extracted_content'

output_fil = 'example'

shutil.make_archive(output_fil,'zip',dir_to_zip)

# to extract the zip file
shutil.unpack_archive('example.zip','final_unzip','zip')