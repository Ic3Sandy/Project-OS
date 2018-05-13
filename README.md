# Project CN341 OS

## initial

- ใช้ [python3.6.5](https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe) และ [pip](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip) ในเครื่อง(Window)
- ลง library ที่ต้องใช้ pip install -r requirements.txt

### Information

- file Procfile ใช้ run command บน heroku ตอนเริ่มโปรแกรม
- requirements.txt ใช้ในการลง library ที่ต้องใช้
- วิธีทำ requirements.txt ใช้ pip install pipreqs จากนั้นสร้าง file โดยใช้ pipreqs ./ จะได้ file มาตรงนั้น
- ใช้ int(os.environ.get('PORT', 5000)) ในการใช้ port ของ heroku
