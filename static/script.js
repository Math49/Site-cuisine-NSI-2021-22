var $dialog = document.getElementById('mydialog'); 
if(!('show' in $dialog)){ 
    document.getElementById('promptCompat').className = 'no_dialog'; 
}

$dialog.addEventListener('close', function() { 
    console.log('Fermeture. ', this.returnValue); 
}); 