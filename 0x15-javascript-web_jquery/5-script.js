$('div#add_item').click(function () {
  let item = $("<li></li>").text("Item");
  $('.my_list').append(item);
});
