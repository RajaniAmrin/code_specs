var jQuery;

 if (window.jQuery === undefined || window.jQuery.fn.jquery !== '1.7.1') {
   var script_tag = document.createElement('script');
   script_tag.setAttribute("type","text/javascript");
   script_tag.setAttribute("src",
       "http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js");
   if (script_tag.readyState) {
     script_tag.onreadystatechange = function () { // For old versions of IE
         if (this.readyState == 'complete' || this.readyState == 'loaded') {
             scriptLoadHandler();
         }
     };
   } else { // Other browsers
     script_tag.onload = scriptLoadHandler;
   }
   (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag);    
 } else {    
   jQuery = window.jQuery;
   main(); //our main JS functionality
 }


 function scriptLoadHandler() {
   jQuery = window.jQuery.noConflict(true);

   main(); //our main JS functionality
 }
 function main() {     
    var potentials = document.querySelectorAll("[class*=price]");
    console.log("Ready",potentials.length)
    for (var i = 0; i < potentials.length; i++) {
        var potential = potentials[i];
        var act_price=parseFloat(potential.innerText)
        var child_class=potential.className
        
        if ( act_price >= 20 & act_price<100)
        {
            var disc_price=act_price-(act_price*0.2)
            console.log(child_class,act_price,disc_price,document.getElementsByClassName(child_class))
            var newNode = document.createElement("div");
            newNode.setAttribute("style", "color:white; background:#8BC34A");
            newNode.innerHTML=disc_price+" (20% off)"
            potential.parentElement.appendChild(newNode)
        }
        if ( act_price >= 100 & act_price<500)
        {
            var disc_price=act_price-(act_price*0.3)
            console.log(child_class,act_price,disc_price,document.getElementsByClassName(child_class))
            var newNode = document.createElement("div");
            newNode.setAttribute("style", "color:white; background:#8BC34A");
            newNode.innerHTML=disc_price+" (30% off)"
            potential.parentElement.appendChild(newNode)
        } 
        if ( act_price >= 500)
        {
            var disc_price=act_price-(act_price*0.4)
            console.log(child_class,act_price,disc_price,document.getElementsByClassName(child_class))
            var newNode = document.createElement("div");
            newNode.setAttribute("style", "color:white; background:#8BC34A");
            newNode.innerHTML=disc_price+" (40% off)"
            potential.parentElement.appendChild(newNode)
        }        
    }
}