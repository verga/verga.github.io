size(200);

real l=4;

draw((0,0)--(l,0));
draw((-1.2,0)--(0,0), gray+dashed);
draw((l,0)--(l+1.2,0), gray+dashed);

for(int x=0; x<=l; ++x){
  dot((x,0), 6pt+rgb(0, 0, 0.6));
};

label("$x \quad x+1$", (2.68,0.5));
label("$\Delta x$", (0,-0.1)--(1,-0.1));
