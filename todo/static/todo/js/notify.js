var duringTime = document.getElementById("duringTime").value;
var description = document.getElementById("description").value;
var title = document.getElementById("title").value;
function notifyMe() {
  var notification = new Notification(title, {
    tag: "ache-mail",
    body: description,
    icon: "https://daniilknaub.fvds.ru/static/todo/melon_logo.png",
  });
}
function notifySet() {
  if (!("Notification" in window))
    alert("Browser doesn't support notifications");
  else if (Notification.permission === "granted")
    setTimeout(notifyMe, duringTime);
  else if (Notification.permission !== "denied") {
    Notification.requestPermission(function (permission) {
      if (!("permission" in Notification)) Notification.permission = permission;
      if (permission === "granted") setTimeout(notifyMe, duringTime);
    });
  }
}
if (duringTime != 0) {
  notifySet();
}
