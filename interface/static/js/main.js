document.addEventListener('DOMContentLoaded', function () {
    var ApiLogType;
    (function (ApiLogType) {
        ApiLogType[ApiLogType["VALID"] = 0] = "VALID";
        ApiLogType[ApiLogType["ERROR"] = 1] = "ERROR";
        ApiLogType[ApiLogType["INFO"] = 2] = "INFO";
        ApiLogType[ApiLogType["WARNING"] = 3] = "WARNING";
    })(ApiLogType || (ApiLogType = {}));
    var data = [
        {
            'type': ApiLogType.VALID,
            'msg': 'this is a good example'
        },
        {
            'type': ApiLogType.ERROR,
            'msg': 'this is a warningerror example'
        },
        {
            'type': ApiLogType.WARNING,
            'msg': 'this is a warning example'
        }
    ];
    var renderLog = function (log) {
        var container = document.querySelector('.log__container');
        // create row
        var row = document.createElement('div');
        // create timestamp
        var timestamp = document.createElement('span');
        if (log.type == ApiLogType.VALID) {
            timestamp.classList.add('text__green');
        }
        else if (log.type == ApiLogType.WARNING) {
            timestamp.classList.add('text__yellow');
        }
        else if (log.type == ApiLogType.ERROR) {
            timestamp.classList.add('text__red');
        }
        var date = new Date(Date.now());
        var formattedDate = "[".concat(date.getMonth(), "-").concat(date.getDate() + 1, "-").concat(date.getFullYear(), " ").concat(date.getHours(), ":").concat(date.getMinutes(), ":").concat(date.getSeconds(), "] ");
        timestamp.innerText = formattedDate;
        row.appendChild(timestamp);
        // create info
        var msg = document.createElement('span');
        msg.classList.add('text__gray');
        msg.innerText = log.msg;
        row.appendChild(msg);
        container === null || container === void 0 ? void 0 : container.appendChild(row);
    };
    data.forEach(function (el) { return renderLog(el); });
});
