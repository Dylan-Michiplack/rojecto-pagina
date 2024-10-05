<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
  >
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="../static/css/style.css">
  <title>Calculadora de eficiencia energética para hogares inteligentes</title>
</head>
<body>
  <header class="header">
    <div class="header__text">
      <h1>Calcule la eficiencia energética de su hogar</h1>
      <p>Tome la iniciativa y resuelva el problema del consumo excesivo de energía</p>
    </div>
  </header>
  <main>
    {% block content %}
    <h2 class="main__title">Especifique el número de dispositivos que utilizan electricidad:</h2>
    <ul class="list" id="list">
      <!-- Asignación #3 -->
      <li class="list__item">
        <a href="{{size + lig + "/4"}}">
          <img class="item__img" src="../static/img/battery.svg" alt="battery">
          <span>3-5 aparatos</span></a>
      </li>
      <li class="list__item">
        <a href="{{size + lig + "/7"}}">
          <img class="item__img" src="../static/img/battery.svg" alt="battery">
          <span>6-8 aparatos</span></a>
      </li>
      <li class="list__item">
        <a href="{{size + lig + "/12"}}">
          <img class="item__img" src="../static/img/battery.svg" alt="battery">
          <span>10+ aparatos</span></a>
      </li>
      <li class="list__item"></li>
        <a href="{{size + lig + "/0"}}">
          <img class="item__img" src="../static/img/planet_medium.svg" alt="battery">
          <span>sin aparatos</span></a>
      </li>
      <!--  -->
    </ul>
    {% endblock %}
  </main>
  <footer>

  </footer>
</body>
</html>
