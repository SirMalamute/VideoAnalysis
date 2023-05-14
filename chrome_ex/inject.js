const { host, hostname, href, origin, pathname, port, protocol, search } =
  window.location;
if (href.includes("youtube.com/watch?v")) {
  alert("running get req");
  fetch("http://127.0.0.1:5000/?id=" + href.split("?v=")[1])
    .then((response) => {
      //handle response
      console.log(response);
    })
    .then((data) => {
      //handle data
      alert(data);
    })
    .catch((error) => {
      //handle error
      console.log(error);
    });
}
