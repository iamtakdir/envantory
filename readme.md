# Make sure your computer has python installed.

# Development :
### Go to your app directory , where manage.py or  requerments.txt exists.
### open up your cmd or  terminal in the same directory , and paste  those commands 

```sh
pip install -r requirements.txt
```
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```

#### if you have any issue with migration in timestamp just select 1 and paste ,
```sh
timezone.now
```

# Starting Your Server :

```sh
python manage.py runserver 
```
### go to this url : 
```sh
127.0.0.1:8000
```
But You have to login first,
use :
```sh
username : admin
password : 9095
```


## Now interact with your application.

To See Admin Panel 
```sh
127.0.0.1:8000/admin
```
use :
```sh
username : admin
password : 9095
```

# Features of Application :

## Stock Inventory System,
#### 1.  ADD , Remove or Modify .
#### 2.  you will  able to input stock information . 
#### 3.  you will  able to remove stock form existing stock . 
#### 4.  you will  able to update stock and change anything . 
#### 5. Live update with alert system . 
#### 6. Live dashboard system . 
#### 7. You can search and filter anything  . 
#### 8. Admin and Staff has diffrent access level . 

## Now Enjoy your E-Invantory 


