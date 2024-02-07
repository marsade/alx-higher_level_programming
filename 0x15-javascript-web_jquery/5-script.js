$('div#add_item').click(function () {
  const item = $('<li></li>').text('Item');
  $('.my_list').append(item);
});
