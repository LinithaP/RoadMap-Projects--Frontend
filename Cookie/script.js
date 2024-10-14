//check if cookie is stored in local storage
document.addEventListener('DOMContentLoaded', function() {
    if (!localStorage.getItem('popup')){
        document.getElementById('popup').style.display = 'block';
    }
});


//accept cookie popup and close
document.getElementById('acceptCookie').addEventListener('click', function() {
   localStorage.setItem('popup', 'true');
    document.getElementById('popup').style.display= 'none';
});

//reject cookie
document.getElementById('rejectCookie').addEventListener('click', function () {
    document.getElementById('popup').style.display = 'none';
  });