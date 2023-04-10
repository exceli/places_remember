ymaps.ready(init);

function init() {
    var myMap;
    var arrcoords = [];
    // var arrcoords = document.getElementById("arrcoords").value;
    arrcoords.push(document.getElementById("arrcoords").value.split(',').map(string => parseFloat(string)))

    myMap = new ymaps.Map('paleceDetailMap', {
        center: [55.76, 37.64],
        zoom: 9,
        controls: ['zoomControl', 'typeSelector', 'rulerControl']
    });

    for (i = 0; i < arrcoords.length; ++i) {
        pl = new ymaps.Placemark(arrcoords[i]);
        myMap.geoObjects.add(pl);
        console.log(arrcoords[i]);
    }
}
