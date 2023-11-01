// result_script.js
document.addEventListener('DOMContentLoaded', function () {
    var processPid = document.getElementById('processPid').getAttribute('data-pid');
    
    document.getElementById('stopProcessButton').addEventListener('click', function () {
        fetch('/stop_process?process_pid=' + processPid, {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.process_status === 'terminated') {
                alert('프로그램을 종료합니다.');
                window.location.href = '/';
            }
        });
    });

    function checkProcessStatus() {
        fetch('/check_process_status?process_pid=' + processPid)
            .then(response => response.json())
            .then(data => {
                if (data.process_status === 'terminated') {
                    window.location.href = '/';
                }
            });
    }

    checkProcessStatus();
    setInterval(checkProcessStatus, 2000);
});
