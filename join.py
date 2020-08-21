
import os
import zipfile
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(100000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['vjoup.zip.000.NOTES', 'vjoup.zip.001.NOTES', 'vjoup.zip.002.NOTES', 'vjoup.zip.003.NOTES', 'vjoup.zip.004.NOTES', 'vjoup.zip.005.NOTES', 'vjoup.zip.006.NOTES', 'vjoup.zip.007.NOTES', 'vjoup.zip.008.NOTES', 'vjoup.zip.009.NOTES', 'vjoup.zip.010.NOTES', 'vjoup.zip.011.NOTES', 'vjoup.zip.012.NOTES', 'vjoup.zip.013.NOTES', 'vjoup.zip.014.NOTES', 'vjoup.zip.015.NOTES', 'vjoup.zip.016.NOTES', 'vjoup.zip.017.NOTES', 'vjoup.zip.018.NOTES', 'vjoup.zip.019.NOTES', 'vjoup.zip.020.NOTES', 'vjoup.zip.021.NOTES', 'vjoup.zip.022.NOTES', 'vjoup.zip.023.NOTES', 'vjoup.zip.024.NOTES', 'vjoup.zip.025.NOTES', 'vjoup.zip.026.NOTES', 'vjoup.zip.027.NOTES', 'vjoup.zip.028.NOTES', 'vjoup.zip.029.NOTES', 'vjoup.zip.030.NOTES', 'vjoup.zip.031.NOTES', 'vjoup.zip.032.NOTES', 'vjoup.zip.033.NOTES', 'vjoup.zip.034.NOTES', 'vjoup.zip.035.NOTES', 'vjoup.zip.036.NOTES', 'vjoup.zip.037.NOTES', 'vjoup.zip.038.NOTES', 'vjoup.zip.039.NOTES', 'vjoup.zip.040.NOTES', 'vjoup.zip.041.NOTES', 'vjoup.zip.042.NOTES', 'vjoup.zip.043.NOTES', 'vjoup.zip.044.NOTES', 'vjoup.zip.045.NOTES', 'vjoup.zip.046.NOTES', 'vjoup.zip.047.NOTES', 'vjoup.zip.048.NOTES', 'vjoup.zip.049.NOTES', 'vjoup.zip.050.NOTES', 'vjoup.zip.051.NOTES', 'vjoup.zip.052.NOTES', 'vjoup.zip.053.NOTES', 'vjoup.zip.054.NOTES', 'vjoup.zip.055.NOTES', 'vjoup.zip.056.NOTES', 'vjoup.zip.057.NOTES', 'vjoup.zip.058.NOTES', 'vjoup.zip.059.NOTES', 'vjoup.zip.060.NOTES', 'vjoup.zip.061.NOTES', 'vjoup.zip.062.NOTES', 'vjoup.zip.063.NOTES', 'vjoup.zip.064.NOTES', 'vjoup.zip.065.NOTES', 'vjoup.zip.066.NOTES', 'vjoup.zip.067.NOTES', 'vjoup.zip.068.NOTES', 'vjoup.zip.069.NOTES', 'vjoup.zip.070.NOTES', 'vjoup.zip.071.NOTES', 'vjoup.zip.072.NOTES', 'vjoup.zip.073.NOTES', 'vjoup.zip.074.NOTES'],'vjoup.zip')
print('unziping')
with zipfile.ZipFile('vjoup.zip', 'r') as zip_ref:
    zip_ref.extractall('vjoup')
os.remove('vjoup.zip')
os.remove('join.py')
