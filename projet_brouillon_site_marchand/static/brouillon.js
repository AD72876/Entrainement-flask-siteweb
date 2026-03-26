const titre= document.querySelector("#titre");
const sous_titre=document.querySelector("#sous_titre");

const button= document.querySelector("#btn_sous_titre");
button.addEventListener("click",() => {
    sous_titre.classList.toggle("hidden");
    alert("Bouton cliqué");

});


const boutton= document.querySelector("#btn_principal");    
boutton.addEventListener("click",() => {
    titre.classList.toggle("hidden");

});



console.log("JS prêt");


const bouton_nuit= document.querySelector("#dark_mode");

bouton_nuit.addEventListener('click', ()=>{
    document.body.classList.toggle("dark_mode");

});

const produits = document.querySelectorAll(".produits");
const btn_panier = document.querySelector("#panier");

let compteur = 0;

produits.forEach(produit => {
    produit.addEventListener("click", () => {
        compteur++;
        btn_panier.textContent = `Panier (${compteur})`;
    });
});