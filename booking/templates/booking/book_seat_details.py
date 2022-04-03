{% load static %}
{% load widget_tweaks %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>University</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    
    <!-- jQuery and Bootstrap CSS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
    
    <!-- HTMX -->
    <script src="https://unpkg.com/htmx.org@1.6.0"></script>

    
</head>
<body>

    <div class="container mt-4">
        <form action="" method="POST" id="form1">
            {% csrf_token %}
        
            <div> 
                {{ form1.library.label_tag }}
                {% render_field form1.library class="custom-select mb-4" autocomplete="off" hx-get="level/" hx-target="#id_level" %}
            </div>

            <div>
                {{ form1.level.label_tag }}
                {% render_field form1.level class="custom-select mb-4" autocomplete="off" %}
            </div>

            <div> 
                {{form1.date.label_tag}}
                {% render_field form1.date class="custom-select mb-4" autocomplete="off" %}
            </div>

            <div>
                {{form1.start_time.label_tag}}
                {% render_field form1.start_time class="custom-select mb-4" autocomplete="off" %}
            </div>

            <div>
                {{form1.end_time.label_tag}}
                {% render_field form1.end_time class="custom-select mb-4" autocomplete="off" %}
            </div>

            {% comment %} <div>
                {{ form1.seat.label_tag }}
                {% render_field form1.seat class="custom-select mb-4" autocomplete="off" %}
            </div> {% endcomment %}
            
            <input type="submit" value="Load Available Seats" name="seat_detail">

        </form>
    </div>
    
</body>
</html>
