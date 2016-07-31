{% extends "base.tpl" %}
{% block title %}CumSea{% endblock %}
{% block content %}
<form action="search" method="post" class="form-group">
    <div class="row">
    <div class="col-lg-4 col-lg-offset-4">
        <div class="input-group">
            <input name="query" type="text" class="form-control" name="q" placeholder="Search" />
            <span class="input-group-btn">
                <button class="btn btn-default" type="submit">Go!</button>
            </span>
        </div><!-- /input-group -->
    </div><!-- /.col-lg-4 -->
</div><!-- /.row -->
<div class="row loader"></div>
</form>
<div id="output">
</div>

<script>

var form = document.querySelector('form');

form.addEventListener('submit', function (e) {
    $( ".loader" ).css( "opacity", "1" );
    e.preventDefault();

    var xhr = new XMLHttpRequest();
    xhr.ontimeout = function () {
        console.error("The request for " + url + " timed out.");
    };
    xhr.onload = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log('xhr loaded')
                document.getElementById("output").innerHTML = xhr.responseText;
                $( ".loader" ).css( "opacity", "0" );
        } else {
            console.error(xhr.statusText);
        }
        }
    };

    xhr.open('POST', 'search');
    console.log(new FormData(form))
    xhr.send(new FormData(form));
}, false);
</script>
{% endblock %}