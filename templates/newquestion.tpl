<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Necesito un nombre para esto</title>
</head>
<body>
<form id ="question" action="/newquestion" method="post" enctype="multipart/form-data">
    <fieldset>
        <p>Porfavor no uses caracteres especiales(acentos, signos de interrogacion, etc.)</p>
        <label for="number">Numero #:</label>
        <input type="text" id="number" name="number"></input>
        <label for="question">Pregunta:</label>
        <input type="text" id="question" name ="question"></input>
        <label for="answer">Respuesta:</label>
        <textarea id="answer" name ="answer"></textarea>
        <button type="submit">Enviar</button>
    </fieldset>

</body>
</html>
