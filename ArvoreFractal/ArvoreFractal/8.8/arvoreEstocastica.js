// EXERCICIO 8.8

function setup() {
    createCanvas(400, 400);
  }
 
  function draw() {
    background(255);
    translate(width/2, height);
    drawFractal(100, 0.6);
    noLoop();
  }
 
  function drawFractal(len, prob) {
   
    line(0, 0, 0, -len);
    translate(0, -len);
 
    if (len > 2) {
      if (random(1) < prob) {
        push();
        rotate(random(-PI/2, PI/2));
        drawFractal(len*0.66, prob*0.9);
        pop();
      }
     
      if (random(1) < prob) {
        push();
        rotate(random(-PI/2, PI/2));
        drawFractal(len*0.66, prob*0.9);
        pop();
      }
     
     
      drawFractal(len*0.66, prob*0.9);
    }
  }

function mouseClicked(){
  loop();
}