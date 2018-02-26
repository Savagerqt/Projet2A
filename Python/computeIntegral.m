function I = computeIntegral(mat) 


model = createpde() ; 
g=decsg(mat);
geometryFromEdges(model,g); % geometryFromEdges for 2-D


edges = [2:1:(size(mat)-1)/2];
%Conditions de bord : 
%Les murs non chauff�s sont � la temp�rature �xterieure To = 10�C
applyBoundaryCondition(model,'dirichlet','Edge',edges,'u',10);

%Le mur chauff� est modelis� par un flux rentrant , on suppose que l'on a
%mis un radiateur au niveau du mur 
applyBoundaryCondition(model,'neumann','Edge',[1],'q',0,'g',10000);

a = 0;
c=1;
a=0;
f=0;
[u,p,e,t] = adaptmesh(g,model,c,a,f,'Par',0.1,'tripick','pdeadworst','MesherVersion','R2013a');



%Le r�sultat est ainsi renvoy� 
%On calcule l'int�grale de la fonction renvoy�e

coord = p ; % Contient les coordonn�es des sommets 
indices = t ; % Contient les r�f�rences de chaque �l�ment
val = u ; 

% On va calculer l'int�grale en �valuant la valeur de la fonction sur
% chaque petit triangle 

I =0 ; 
area = 0 ; 
for i = 1:length(indices) ; % Pour chaque triangle 
    a = coord(:,indices(1,i)) ;     % Coord du 1er point 
    b = coord(:,indices(2,i)) ;     % Coord du second point 
    c = coord(:,indices(3,i)) ;     % Coorddu troisi�me point
    
    moy = (val(indices(1,i))+val(indices(1,i))+val(indices(1,i)))/3 ;
    area = area + 0.5*abs(a(1)*c(2)-a(1)*b(2)+b(1)*a(2)-b(1)*c(2)+c(1)*b(2)-c(1)*a(2)) ; 
    I = I + moy*0.5*abs(a(1)*c(2)-a(1)*b(2)+b(1)*a(2)-b(1)*c(2)+c(1)*b(2)-c(1)*a(2)) ;
end
    I = I/area ; 
