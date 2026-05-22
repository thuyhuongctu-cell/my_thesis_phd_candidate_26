//write tampemonkey script to open all links in a new tab
// ==UserScript==
// @name         Google Scholar Link Opener
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Francoo86
// @match        https://scholar.google.com/*
// @grant        none
// ==/UserScript==

const CURRENT_PAGE_CLASS = "gs_ico gs_ico_nav_current";
const MAX_EXPLORED_PAGES = 990;

function addDownloadPageButton() {
    const buttonsNav = document.getElementById("gs_ab_btns");

    const downloadButton = document.createElement("a");
    downloadButton.id = "downloadButton";
    downloadButton.href = "#";
    downloadButton.innerHTML = "Descargar página";
    downloadButton.style.backgroundColor = "white";
    downloadButton.style.color = "blue";
    downloadButton.onclick = function() {
        const pageContent = document.documentElement.innerHTML;
        const pageContentWithHtmlTag = `<!DOCTYPE html><html>${pageContent}</html>`;
        const blob = new Blob([pageContentWithHtmlTag], { type: "text/html" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;

        let start = window.location.href.split("start=")[1];

        if(start) {
            //remove everything after the start
            start = start.split("&")[0];
            start = start.slice(0, -1);
        }

        a.download = `page_${start ? start : 0}.html`;
        a.click();
        URL.revokeObjectURL(url);

        if(!areLinksSwapable()) {
            window.close();
        }
    };

    buttonsNav.appendChild(downloadButton);

    document.addEventListener("keydown", function(event) {
        if (event.key === "k") {
            downloadButton.click();
        }
    });
}

function areLinksSwapable() {
    //check if we have https://scholar.google.com/scholar?start= after 'start=' we have numbers ending with '90' in browser link
    const start = window.location.href.split("start=")[1];

    if(!start){
        return false;
    }

    const startNumber = start.split("&")[0];
    return startNumber.endsWith("90");
}

function getAllLinks(boom) {
    const navBar = document.getElementById("gs_n");
    const links = navBar.getElementsByTagName("a");

    if (!navBar) {
        console.log("No nav bar found");
        return;
    }
    
    const linksArray = [];
    const footer = document.getElementById("gs_ftr_rt");
    const openLinks = document.createElement("a");
    openLinks.href = "#";
    openLinks.innerHTML = "Abrir todos los enlaces";
    openLinks.style.color = "blue";

    if(areLinksSwapable()){
        //supposing in the browser we have something ending with '90' we can swap the links
        const currentPage = links[1];
        currentPage.className = CURRENT_PAGE_CLASS;
        const span = document.createElement("span");
        span.innerHTML = currentPage.innerHTML;
        currentPage.parentNode.replaceChild(span, currentPage);

        //get the start= number from the current page
        const start = window.location.href.split("start=")[1];
        const startNumber = start.split("&")[0];
        
        //for next links we will add 10 to the start number
        let newStartNumber = parseInt(startNumber) + 10;
        for (let i = 0; i < links.length; i++) {
            if (newStartNumber > MAX_EXPLORED_PAGES) {
                break;
            }

            const link = links[i];
            //replace the href that has "start=somenumber" with the new start number
            const newHref = link.href.replace(/start=\d+/, `start=${newStartNumber}`);
            //add the new href to the array
            linksArray.push(newHref);
            newStartNumber += 10;
        }

        openLinks.style.backgroundColor = "yellow";
        openLinks.onclick = () => {
            boom.play();
        }

        document.title = "VERY IMPORTANT PAGE!!!!"
    }
    else {
        for (let i = 0; i < links.length; i++) {
            if (linksArray.indexOf(links[i].href) === -1 && links[i].href !== window.location.href) {
                linksArray.push(links[i].href);
            }
        }
    }

    openLinks.onclick = () => {
        let captchaExists = false;
        const currentContext = window;

        linksArray.forEach(link => {
            if(captchaExists) {
                currentContext.alert("CAPTCHA DETECTADO RESUELVELO Y VUELVE A INTENTARLO");
                return;
            }
            //open each one but with a delay between 1-3 seconds
            //avoid bot detection
            setTimeout(() => {
                const proxy = window.open(link, "_blank");

                proxy.onload = (e) => {
                    //wait a little bit to download the page to press the download button
                    setTimeout(() => {
                        //i hate stoopid captchas
                        const captcha = proxy.document.getElementById("gs_captcha_c");

                        if(captcha) {
                            captchaExists = true;
                            proxy.close();
                            return;
                        }

                        if(proxy.document.title === "VERY IMPORTANT PAGE!!!!") {
                            return;
                        }

                        //check if there is any data-lid attribute
                        const dataLid = proxy.document.querySelector("[data-lid]");

                        if(dataLid) {
                            proxy.document.getElementById("downloadButton").click();
                        }

                        //we don't need the page anymore
                        proxy.close();
                    }, 1000);
                };

            }, Math.floor(Math.random() * 3000) + 1000);
            //window.open(link, "_blank");
        });
    };

    footer.appendChild(openLinks);
    footer.insertBefore(openLinks, footer.firstChild);
    //print links on console
    console.log(linksArray);
}
(function() {
    'use strict';
    const BOOM_AUDIO = new Audio("https://www.myinstants.com/media/sounds/vine-boom.mp3");
    addDownloadPageButton();
    getAllLinks(BOOM_AUDIO);
})();