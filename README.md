# Project CN341 OS

## initial

- ใช้ [python3.6.5](https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe) และ [pip](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip) ในเครื่อง(Window)
- ลง library ที่ต้องใช้ pip install -r requirements.txt

### Information

- การเขียน [Sockets](https://www.tutorialspoint.com/python3/python_networking.htm) และ [Multithreaded](https://www.tutorialspoint.com/python3/python_multithreading.htm)
- file Procfile ใช้ run command บน heroku ตอนเริ่มโปรแกรม
- requirements.txt ใช้ในการลง library ที่ต้องใช้
- วิธีทำ requirements.txt ใช้ pip install pipreqs จากนั้นสร้าง file โดยใช้ pipreqs ./ จะได้ file มาตรงนั้น
- ใช้ int(os.environ.get('PORT', 5000)) ในการใช้ port ของ heroku
- เรียนรู้การใช้ [jQuery AJAX](https://www.w3schools.com/jquery/jquery_ref_ajax.asp) ในการทำหน้า html
