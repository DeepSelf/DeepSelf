/* 
 This script has been written for Deepself's website.
 It uses the module Waypoints : http://imakewebthings.com/waypoints/guides/getting-started/
 */


                                /* =====================================
                                ============== Variables ===============
                                ======================================*/


var bars_to_fill_scroll = document.getElementsByClassName('bar-to-fill-scroll');
var develops_hover = document.getElementsByClassName('develop-hover');

var widthMap = new Map(); // Map containing the wished width of the progress bars we have to fill
var waypoints = []; // Array containing the waypoints spotted on the page
var heightMap = new Map(); // Map containing the wished height of the elements we have to develop
var mouseOverMap = new Map(); // Map containing booleans indicating if the mouse is over an element


                                /* =====================================
                                ============== Functions ===============
                                ======================================*/



// gets all elements with class 'bar-to-fill-appear' in all the childNodes levels of an element elt. this function
// must be used on an element with class 'bars-to-develop'
function get_bars(elt) {
    if (elt.classList.contains('bar-to-fill-appear')) {
        return [elt];
    }
    else {
        if (elt.children.length > 0) {
            barsArray = [];
            for (let child of elt.children) {
                barsArray = barsArray.concat(get_bars(child));
            }
            return barsArray;
        }
        else {
            return [];
        }
    }
}

                                /* =====================================
                                ============== Animations ==============
                                ======================================*/


// starts an animation which fills the progress bar (width=0 => width=targetWidth)
function fill(bar) {
    let speed = widthMap.get(bar)/10;
    let animationId = null;
    
    function fillBar() {
        let width = parseFloat(getComputedStyle(bar).width);
        if (width + speed <= widthMap.get(bar)) {
            bar.style.width = (width + speed) + "px";
            animationId = requestAnimationFrame(fillBar);
        }
        else {
            bar.style.width = widthMap.get(bar)
            cancelAnimationFrame(animationId);
        }
    }
    
    animationId = requestAnimationFrame(fillBar);
}


// starts an animation which makes appear the element elt (opacity=0 => opacity=1)
function appear_elt(elt) {
    let speed = 1/20;
    let animationId = null;
    
    function appearElt() {
        let opacity = parseFloat(getComputedStyle(elt).opacity);
        if (opacity + speed <= 1.0 && mouseOverMap.get(elt.parentNode)) {
            elt.style.opacity = (opacity + speed);
            animationId = requestAnimationFrame(appearElt);
        }
        else {
            if (mouseOverMap.get(elt.parentNode)) {
                elt.style.opacity = 1.0;
                if (elt.classList.contains('bars-to-develop')) {
                    let bars_to_develop = get_bars(elt);
                    for (let bar of bars_to_develop) {
                        let percent = parseFloat(bar.parentNode.getAttribute('data-percent'));
                        widthMap.set(bar, parseFloat(getComputedStyle(bar.parentNode).width) * percent / 100);
                        fill(bar);
                    }
                }
            }
            cancelAnimationFrame(animationId);
        }
    }
    
    animationId = requestAnimationFrame(appearElt);
}


// starts an animation which makes disappear element elt (opacity=1 => opacity=0)
function disappear_elt(elt) {
    let speed = 1/10;
    let animationId = null;
    
    function disappearElt() {
        let opacity = parseFloat(getComputedStyle(elt).opacity);
        if (opacity - speed >= 0.0 && !mouseOverMap.get(elt.parentNode)) {
            elt.style.opacity = (opacity - speed);
            animationId = requestAnimationFrame(disappearElt);
        }
        else {
            if (!mouseOverMap.get(elt.parentNode)) {
                elt.style.opacity = 0.0;
                close_elt(elt);
            }
            cancelAnimationFrame(animationId);
        }
    }
    
    animationId = requestAnimationFrame(disappearElt);
}


// starts an animation which makes growing the element elt (height=0 => height=targetHeight)
function develop_elt(elt) {
    let speed = heightMap.get(elt)/10;
    let animationId = null;
    
    function developElt() {
        let height = parseFloat(getComputedStyle(elt).height);
        if (height + speed < heightMap.get(elt) && mouseOverMap.get(elt.parentNode))  {
            elt.style.height = (height + speed) + "px";
            animationId = requestAnimationFrame(developElt);
        }
        else {
            if (mouseOverMap.get(elt.parentNode)) {
                elt.style.height = heightMap.get(elt) + "px";
                appear_elt(elt);
            }
            cancelAnimationFrame(animationId);
        }
    }
    
    animationId = requestAnimationFrame(developElt);
}


// starts an animation which reduces the element elt (height=initialHeight => height=0)
function close_elt(elt) {
    let speed = heightMap.get(elt)/5;
    let animationId = null;
    
    function closeElt() {
        let height = parseFloat(getComputedStyle(elt).height);
        if (height - speed > 0 && !mouseOverMap.get(elt.parentNode)) {
            elt.style.height = (height - speed) + "px";
            animationId = requestAnimationFrame(closeElt);
        }
        else {
            if (!mouseOverMap.get(elt.parentNode)) {
                elt.style.height = "0px";
                elt.style.display = 'none';
            }
            cancelAnimationFrame(animationId);
        }
    }
    
    animationId = requestAnimationFrame(closeElt);
}


                                /* =====================================
                                ======= Variables' manipulation ========
                                ======================================*/



for (let bar_to_fill of bars_to_fill_scroll) {
    let percent = parseFloat(bar_to_fill.parentNode.getAttribute('data-percent'));
    widthMap.set(bar_to_fill, parseFloat(getComputedStyle(bar_to_fill.parentNode).width) * percent / 100);
    waypoints.concat([new Waypoint({
                        element: bar_to_fill,
                        handler: function(){
                            fill(bar_to_fill)
                        },
                        offset: window.innerHeight - bar_to_fill.style.height
                        })]);
}

for (let develop_hover of develops_hover) {
    heightMap.set(develop_hover, parseFloat(getComputedStyle(develop_hover).height));
    develop_hover.style.opacity = 0;
    develop_hover.style.height = 0;
    develop_hover.style.display = 'none';
    develop_hover.parentNode.addEventListener('mouseover', function(){
        console.log('mouse over')
        console.log(develop_hover.parentNode)
        develop_hover.style.display = 'flex';
        mouseOverMap.set(develop_hover.parentNode, true);
        develop_elt(develop_hover);
    })
    develop_hover.parentNode.addEventListener('mouseleave', function() {
        console.log('mouse left')
        console.log(develop_hover.parentNode)
        mouseOverMap.set(develop_hover.parentNode, false);
        disappear_elt(develop_hover);
    })
}







