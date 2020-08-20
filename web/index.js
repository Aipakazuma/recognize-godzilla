const selectElement = document.querySelector('#file-upload');
const url = 'http://localhost:81/upload'
selectElement.addEventListener('change', (event) => {
    var reader = new FileReader();
    reader.onload = function(e) {
        var preview = document.querySelector('#preview')
        preview.src = e.target.result;
    }
    var file_obj = event.target.files[0];
    if (file_obj.name.toLowerCase().match(/\.(jpeg|jpg|png|gif)/)) {
        reader.readAsDataURL(file_obj);
        post();
    } else {
        alert('画像ファイルを選択してください.');
    }
});

function post() {
    var params = new FormData();
    params.append('file', selectElement.files[0]);
    axios.post(url, params)
        .then(function(response) {
            // 成功時
            console.log(response);
            plot(response);
        })
        .catch(function(error) {
            // エラー時
            console.log(error);
        });
}

function plot(res) {
    option = {
        yAxis: {
            type: 'category',
            data: ['Not', 'Godzilla']
        },
        xAxis: {
            type: 'value'
        },
        series: [{
            data: [res.data.y_pred_proba_0,
                   res.data.y_pred_proba_1],
            type: 'bar'
        }]
    };
    var myChart = echarts.init(document.getElementById('probablity'));
    myChart.setOption(option);
}
