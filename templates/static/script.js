function scrollToApp() {
    document.getElementById("app").scrollIntoView();
}

async function sendRequest() {
    let mode = document.getElementById("mode").value;
    let input = document.getElementById("input").value;

    let loading = document.getElementById("loading");
    let output = document.getElementById("output");

    loading.style.display = "block";
    output.innerText = "";

    let body = {};

    if (mode === "chat") body = { message: input };
    else if (mode === "quiz") body = { topic: input };
    else if (mode === "planner") body = { subjects: input, date: "2026-04-01" };
    else body = { text: input };

    let res = await fetch("/" + mode, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
    });

    let data = await res.json();

    loading.style.display = "none";
    output.innerText = data.response;
}