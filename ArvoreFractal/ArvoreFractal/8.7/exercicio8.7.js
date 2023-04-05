// EXERCICIO 8.7
function setup() {
    createCanvas(600, 600);
  }
  
  function draw() {
    background(255);
    
    translate(width/2, height);
    
    drawFractal(10, 100)
  }
  
  function drawFractal(grossura,len) {
    
      strokeWeight(grossura);
      line(0,0,0,-len);
      translate(0,-len);
  
  if (len >5) {
      drawFractal(grossura*0.8, len*0.66)
  push();
    rotate(PI/6);
    drawFractal(grossura*0.8, len*0.66)
  pop();
    
    push();
    rotate(-PI/6);
    drawFractal(grossura*0.8, len*0.66)
    pop();
  }
  }  
