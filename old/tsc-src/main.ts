document.addEventListener( 'DOMContentLoaded', () => {
    enum ApiLogType {
        VALID,
        ERROR,
        INFO,
        WARNING
    }
    
    interface IApiLog {
        'type': ApiLogType,
        'msg': string
    }
    
    let data: IApiLog[] = [
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
    ]
    
    const renderLog = (log: IApiLog) => {
        const container = document.querySelector( '.log__container' )
    
        // create row
        const row = document.createElement( 'div' )
    
        // create timestamp
        const timestamp = document.createElement( 'span' )
    
        if (log.type == ApiLogType.VALID) {
            timestamp.classList.add( 'text__green' )
        } else
        if (log.type == ApiLogType.WARNING) {
            timestamp.classList.add( 'text__yellow' )
        } else
        if (log.type == ApiLogType.ERROR) {
            timestamp.classList.add( 'text__red' )
        }
    
        const date = new Date(Date.now());
        const formattedDate = `[${date.getMonth()}-${date.getDate() + 1}-${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}] `
    
        timestamp.innerText = formattedDate
    
        row.appendChild( timestamp )
        
    
        // create info
        const msg = document.createElement( 'span' )
        msg.classList.add( 'text__gray' )
        msg.innerText = log.msg
    
        row.appendChild( msg )
    
        container?.appendChild( row )
    }
    
    data.forEach((el) => renderLog( el ))

    // main loop
    // TODO: state should be available through api, copying run structure
    let stop: boolean = false

    while (!stop) {

    }
})
