# Documentation for the FaceMark App API.
<b>`url`</b> = <i>`
http://165.232.178.109:8000/  `</i> 

## Login Page
### Login User
<b>POST</b>     `url`/dj-rest-auth/login/<br>
Input      
"email": "example@email.com"<br>
"password": "password@123"

---

## Home Page
### Fetch Branches
<b>GET</b>    `url`/api/branch/

### Fetch  Subjects
<b>GET</b>    `url`/api/subject/

### Fetch Section
<b>GET</b>    `url`/api/section/

---

## Image Preview Page
### Send Image
<b>POST</b>  `url`/face/present/<br>
Input
"image": "path/to/image/image.jpg"<br>
Output <br>
List of usns of students present in the image

---

## Profile Settings Page
### Sign Out
<b>POST</b> `url`/dj-rest-auth/logout/<br>

## Change Password
### New Password
<b>POST</b> `url`/dj-rest-auth/password/change/<br>

## Send Attendance Report
### send mail
<b>GET</b> `url`/api/send_mail/

---

## Update Attendance
### Update Attendance
<b>PUT</b> `url`/api/attendance/\<id> <br>
