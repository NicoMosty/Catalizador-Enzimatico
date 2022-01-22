<h1 align="center">
    Transferencia simultánea de masa & reacción bioquímica en el soporte esférico
</h1>

A continuación se muestra la ecuación diferencial que representa la transferencia simultanea de masa y reacción química dentro del biocatalizador enzimático, donde:

<div align="center"><img style="background: white;" src="eq\BmqQnjNriH.svg"></div>

Para el caso del radio inicial 
<span align="center"><img style="background: white;" src="eq\df5Zwv1KvJ.svg"></span>

<div align="center"><img style="background: white;" src="eq\a3OeoYVWBx.svg"></div>

Para poder hallar la distribución se utiliza la siguiente distribución con tablas, donde: 
<div align="center"><img style="background: white;" src="eq\Screenshot_1.png"></div>

Se puede ver en la tabla que se supone un valor de <span align="center"><img style="background: white;" src="eq\qll8hwB79R.svg"></span> (naranja)y se modifica hasta que el valor en <span align="center"><img style="background: white;" src="eq\24HlDziO7A.svg"></span> sea igual a 1.

Para hacer lo anterior se definen los siguientes invervalos de <span align="center"><img style="background: white;" src="eq\NG6Wf3CbzN.svg"></span> , donde:

<div align="center"><img style="background: white;" src="eq\pRHcd00R4e.svg"></div>

<div align="center"><img style="background: white;" src="eq\ZPrwbSIlio.svg"></div>

Para poder realizar el calculo se definió un <span align="center"><img style="background: white;" src="eq\WrAgk89JJb.svg"></span>

Para calcular lo anterior se realizó un algoritmo en *Python*. El código se
encuentra en el siguiente link:


<a href="SvsR.py">
    <p align="center">
        Programa en Python (Concentración Sustrato vs Radio)
    </p>
</a>
<div align="center">
    El programa se llama SvsR.py.py
</div>

Los resultados se muestran a continuación:

<div align="center"><img style="background: white;" src="S-vs-r/Beta-10.0.png"></div>
<div align="center"><img style="background: white;" src="S-vs-r/Beta-5.0.png"></div>
<div align="center"><img style="background: white;" src="S-vs-r/Beta-1.0.png"></div>
<div align="center"><img style="background: white;" src="S-vs-r/Beta-0.5.png"></div>
<div align="center"><img style="background: white;" src="S-vs-r/Beta-0.1.png"></div>
<div align="center"><img style="background: white;" src="S-vs-r/Beta-0.05.png"></div>
<div align="center"><img style="background: white;" src="S-vs-r/Beta-0.01.png"></div>

---

<h4 align="center">
    Cálculo del Factor de Efectividad (μ)
</h1>
 
 Para el calculo del factor de efectividad se tiene la siguiente ecuación:

<div align="center"><img style="background: white;" src="eq\ipULTE2L4e.svg"></div>

Donde se tienen los siguientes valores

<div align="center"><img style="background: white;" src="eq\jY2H7WsER5.svg"></div>

Para el cálculo se requiere de la derivada de la concentración en la superficie externa del biocatalizador esférico, donde este valor fue encontrado anteriormente. Para hacer lo anterior se definen los siguientes invervalos de 𝛽 y 𝜙, donde:

<div align="center"><img style="background: white;" src="eq\a2GAzenuir.svg"></div>

Para calcular lo anterior se realizó un algoritmo en Python (El código se encuentra en el siguiente link)

<a href="Ef.py">
    <p align="center">
        Programa en Python (Factor de Efectividad)
    </p>
</a>
<div align="center">
    El programa se llama Ef.py
</div>

El resultado hallado se encuentra a continuación:

<div align="center"><img style="background: white;" src="Phi^Beta-vs-Ef.png"></div>