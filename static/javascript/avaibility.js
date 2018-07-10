function change_classes(){
    var elements = document.getElementsByTagName('td');

    for (let index = 0; index < elements.length; index++) {
      
        if(elements[index].innerHTML == 1){
            elements[index].className = 'bg-success';
            elements[index].innerHTML = 'DISPONIBLE';
        }if(elements[index].innerHTML == 0){
            elements[index].className = 'bg-danger';
            elements[index].innerHTML = 'C MAMUT :(';
        }
        
        
    }
}

