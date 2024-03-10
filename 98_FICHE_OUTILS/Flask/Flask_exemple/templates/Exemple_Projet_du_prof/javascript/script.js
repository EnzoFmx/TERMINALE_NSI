//alert("Voici une alerte javascript")

function change_couleur(){
	document.getElementById('test').style.color='blue';
}

//change_couleur(); //Comme en python, il suffit de l'appeler

document.getElementById('but').addEventListener('click',change_couleur);

