<div style="padding: 2% 5%;">

<h1 style="text-align: center;">
<div style="color:grey; font-size: 0.6em;">Jakub Ostrzołek</div>
<div>WMM - lab. 8 - Generowanie grafiki</div>
</h1>

## Składanie transformacji (robot)
To zadanie zostało przeze mnie wykonane w ramach stacjonarnych laboratoriów.

## Cieniowanie
Tak jak wskazano w instrukcji, w programi dostępne są następujące parametry:
* w shaderze (`phong.frag`):
  * `light_position` - pozycja źródła światła
  * `ambient_light_color` - kolor światła otoczenia
  * `ambient_strength` - współczynnik otoczenia
  * `diffuse_strength` - współczynnik rozproszenia
  * `specular_strength` - współczynnik odbicia
* w programie (`phong_window.py:init_shaders_variables`):
  * `obj_color` - kolor obiektu
  * `diffuse_light_color` - kolor światła rozproszenia
  * `specular_light_color` - kolor światła odbicia
  * `shininess` - współczynnik połyskiwości

Poniżej przedstawiono wpływ tych ustawień na renderowaną grafikę.
* początkowe ustwienia  
![](1.png)
* zmiana kierunku światła  
![](2-light-direction.png)
* zmiana koloru obiektu  
![](4-obj-color.png)
* zmiana koloru światła otoczenia  
![](3-ambient-color.png)
* zmiana koloru rozproszenia światła  
![](5-diffuse-light-color.png)
* zmiana koloru odbicia światła  
![](6-specular-light-color.png)
* zmiana współczynnika otoczenia  
![](7-ambient-strength.png)
* zmiana współczynnika rozproszenia  
![](8-diffuse-strength.png)
* zmiana współczynnika odbicia  
![](9-specular-strength.png)
* zmiana współczynnika połyskliwości  
![](10-shininess.png)


</div>