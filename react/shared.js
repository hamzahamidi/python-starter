


fetch(url).then((response) => {
    if (response.ok) {
        return response.json();
    } else {
        throw new Error('Something went wrong');
    }
})
    .then((responseJson) => {
        // Do something with the response
    })
    .catch((error) => {
        console.log(error)
    });



const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ${inMemoryToken}'

        // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
});


https://easyepargne-recprj.axa-fr.intraxa/clauseBeneficiaire/?Client=341739392&Contrats=8602944181&Dossier=CRMSF290421CB145
export const getSearchParams = () => {
    const searchParams = new URLSearchParams(window.location.search);
    const numeroClient = searchParams.get('Client');
    const dossierSFO = searchParams.get('Dossier');
    const contratSFO = searchParams.get('Contrats');
    const acte = searchParams.get('Acte');
    return {
      numeroClient,
      dossierSFO,
      contratSFO,
      acte,
    };
  };
  


  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error
  // https://developer.mozilla.org/en-US/docs/Web/API/Response/status
  class CustomError extends Error {
    constructor(foo = 'bar', ...params) {
      // Pass remaining arguments (including vendor specific ones) to parent constructor
      super(...params)
  
      // Maintains proper stack trace for where our error was thrown (only available on V8)
      if (Error.captureStackTrace) {
        Error.captureStackTrace(this, CustomError)
      }
  
      this.name = 'CustomError'
      // Custom debugging information
      this.foo = foo
      this.date = new Date()
    }
  }
  
  try {
    throw new CustomError('baz', 'bazMessage')
  } catch(e) {
    console.error(e.name)    //CustomError
    console.error(e.foo)     //baz
    console.error(e.message) //bazMessage
    console.error(e.stack)   //stacktrace

    if (e instanceof CustomError) {
        // specific error
       } else {
          // let others bubble up
       }

  }