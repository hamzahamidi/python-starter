
setInterval(async function () {
    const reponse = await fetch("https://www.dealabs.com/mascotcards/see", {
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,fr;q=0.8,ar;q=0.7",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "x-xsrf-token": "xI1zqZFnDhXsChSwnF86iSHHwEpkMTEY9vowjI1T"
        },
        "referrer": "https://www.dealabs.com/hot",
        "referrerPolicy": "strict-origin-when-cross-origin",
        "body": null,
        "method": "GET",
        "mode": "cors",
        "credentials": "include"
    })
    const { data } = await reponse.json();
    const { content: input } = data;

    if (input) {
        console.log(new Date());
        const a = "8f5901ca6abd188918f9106dfc94c5d8".length;
        const b = "mascotcards-".length

        const begin = input.indexOf("mascotcards-")
        const key = input.slice(begin, begin + a + b);


        const response = await fetch("https://www.dealabs.com/mascotcards/claim", {
            "headers": {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9,fr;q=0.8,ar;q=0.7",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "pragma": "no-cache",
                "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Linux\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest",
                "x-xsrf-token": "TLm4avDQ0XBE9mloQozhtiAD4faii5GAYIIwbD1c"
            },
            "referrer": "https://www.dealabs.com/",
            "referrerPolicy": "strict-origin-when-cross-origin",
            "body": `key=${key}`,
            "method": "POST",
            "mode": "cors",
            "credentials": "include"
        });
        const data = await response.json();
        console.log(data);

    }
 
}, 1500)