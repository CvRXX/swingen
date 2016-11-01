$(function() {

    Morris.Line({
        element: 'morris-line-chart',
        data: [
	
	{% for i in waveData %}
	{
            period: '{{loop.index}}',
            wave: {{i[0]}},
        }, 
	{% endfor %}	
        ],
        xkey: 'period',
        ykeys: ['wave'],
        labels: ['wave'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

});
