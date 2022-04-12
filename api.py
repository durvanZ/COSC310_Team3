myApiKey = 'bfa6af7b507f764a24747a4ae33a004b';

data = {
  method: 'flickr.photos.search',
  api_key: myApiKey,
  text: 'cat',
  sort: 'interestingness-desc',
  per_page: 12,
  license: '4',
  extras: 'owner_name,license',
  format: 'json',
  nojsoncallback: 1,
};

parameters = newURLSearchParams(data);

url = `https://api.flickr.com/services/rest/?${parameters}`;
console.log(url);

onst getFlickrImageURL = (photo, size) => {
  let url = `https://farm${photo.farm}.staticflickr.com/${photo.server}/${photo.id}_${
    photo.secret
  }`;
  if (size) {
    // Configure image size
    url += `_${size}`;
  }
  url += '.jpg';
  return url;
};

const url = `https://api.flickr.com/services/rest/?${parameters}`;

axios.get(url)
  .then(response => response.json())
  .then(data => (
    // get an array of image-url
    data.photos.photo.map((photo) => {
      return getFlickrImageURL(photo, 'q');
    })
  ));

