<div class="card-deck-wrapper">
  <div class="card-deck">
{% for result in results %}
    <div class="card col-md-6 card-inverse">
        <div class="card-block">
            <h4 class="card-title"> {{result[0].title}} </h4>
            <a href="{{result[0].url}}" class="card-link">{{result[0].url}}</a>
            <p class="card-text"> {{result[0].body}} </p>
        </div>
    </div>
    <div class="card col-md-6"">
        <div class="card-block">
            <h4 class="card-title"> {{result[1].title}} </h4>
            <a href="{{result[1].url}}" class="card-link">{{result[1].url}}</a>
            <p class="card-text"> {{result[1].body}} </p>
        </div>
    </div>
  </div>
</div>
{% endfor %}