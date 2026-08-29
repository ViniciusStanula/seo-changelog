# Product data specification

Use this guide to format your product information for Merchant Center. Google uses this data to match your products to the right queries, and as a foundational input to help optimize and enhance the content of the ads being served in our AI powered formats and experiences. Providing accurate and correctly formatted product data is essential for creating successful ads and free listings, and for preventing product disapprovals or display issues.

Incorrect, inaccurate, or missing product information can cause disapprovals, limited eligibility, incorrect displays for your products, or other [ Issues in Merchant Center](https://support.google.com/merchants/answer/12153802). Common problems include, incorrect google product category `[google_product_category] `or gtin `[gtin]` attribute values, missing or incorrect variant attributes (such as item group id `[item_group_id]`, color `[color]` or size `[size]`), low-quality images, or conflicting data between your feed and website. These issues can prevent your ads and free listings from showing on Google.

**Note** : In the Issue Details Page (IDP) of your Merchant Center account, you can view all the diagnostic information for any issues affecting your products. It will allow you to more easily identify, understand, and resolve issues. Learn more [About the Issue Details Page](https://support.google.com/merchants/answer/16431300).

**On this page**

* Before you begin
* Definitions

### Product data attributes:

* Basic product data
* Price and availability
* Product category
* Product identifiers
* Detailed product description
* Shopping campaigns and other configurations
* Marketplaces
* Destinations
* Shipping and returns

* * *

## Before you begin

Other requirements

In addition to this product data specification, your product data must also meet the following requirements:

* [**Shopping ads policies**](https://support.google.com/merchants/answer/6149970)
* [**Landing page requirements**](https://support.google.com/merchants/answer/4752265)
* [**Shipping rate data requirements**](https://support.google.com/merchants/answer/12570809)
* [**Checkout requirements and best practices**](https://support.google.com/merchants/answer/9158778)
* [**Currency and language requirements**](https://support.google.com/merchants/answer/160637)

Formatting your product data

Use English when submitting the names of attributes and the values for attributes that use supported values. For example, the condition `[condition]` attribute uses the supported values `new`, `refurbished`, and `used`, which must be submitted in English in order for the system to read them.

For all attributes that don't use supported values, but rather allow for free form text, such as the title `[title]` or description `[description]` attributes, be sure to use the same language for all attributes in a feed. Use an underscore when submitting an attribute name with multiple words (for example, `image_link`). Learn how to [Submit attributes and attribute values](https://support.google.com/merchants/answer/10668075)

* * *

## Definitions

* **Product** : This is the actual product that potential customers search for on Google.
* **Item** : This is a product that has been added to your product data, either in a text feed, XML feed, or API. For example, an item is one line in your text feed.
* **Variant** : These are specific versions of a product that comes in different variations. For example, a shirt that comes in different sizes has size variants.

**Required** : Submit this attribute. If you don't, your product won't be able to serve in ads and free listings.

**It depends** : You may or may not need to submit this attribute depending on the product or the countries in which your products show.

**Optional** : You can submit this attribute if you want to help boost your product's performance.

## Basic product data

The product information you submit using these attributes is the foundation for creating successful ads and free listings for your products. Make sure everything you submit is of the quality you'd show to a customer.

**Label assets that are AI edited or created**

AI regulations in the European Union, India, and New York require that ads with certain AI-generated or edited assets include disclosures and/or labels that inform consumers that the ads were made with AI.

Add labels directly to your creatives or use the AI label setting in Google Ads, Display & Video 360, Campaign Manager 360, Merchant Center, and Ads Editor to add AI labels to your creatives. Learn more about how to [Use AI content label settings to label your ads](https://support.google.com/google-ads/answer/17140115).

**Notes**

* These labels will not be in violation of [Google policies prohibiting text overlays](https://support.google.com/adspolicy/answer/10347108) and watermarks.
* Use of the AI label setting in Google’s advertising products doesn't guarantee your compliance with specific regulations. Seek legal guidance and take measures as needed to [ensure your ads and assets follow all local legal obligations and policies](https://support.google.com/adspolicy/answer/6023676)

**Attribute and format** |  **Minimum requirements at a glance**
---|---
[ID `[id]`](https://support.google.com/merchants/answer/6324405) Your product’s unique identifier **Required** **Example**
`A2B4` **Syntax**
Max 50 characters **Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Use a unique value for each product.
* Use the product's SKU where possible.
* Keep the ID the same when updating your data.
* Use only valid unicode characters.
* Use the same ID for the same product across countries or languages.

[Title `[title]`](https://support.google.com/merchants/answer/6324415) or [Structured title `[structured_title]`](https://support.google.com/merchants/answer/6324415) Your product’s name **Required** Example ([Title `[title]`](https://support.google.com/merchants/answer/6324415)):
Mens Pique Polo Shirt Example ([Structured title `[structured_title]`](https://support.google.com/merchants/answer/6324415)): `trained_algorithmic_media:"Stride & Conquer: Original Google Men's Blue & Orange Power Shoes (Size 8)"` **Syntax**
[Title `[title]`](https://support.google.com/merchants/answer/6324415): Plain text.Max 150 characters [Structured title `[structured_title]`](https://support.google.com/merchants/answer/6324415): 2 sub-attributes:

* Digital source type `[digital_source_type]` (**Optional**): This sub-attribute supports 2 values:
* Default `[default]`: Specifies that the title provided using the content `[content]` sub-attribute was **not** created using generative AI.
* Trained algorithmic media `[trained_algorithmic_media]`. Specifies that the title provided using the content `[content]` sub-attribute was created using Generative AI.

If no value is specified, the Default `[default]` value is used.

* Content `[content]` (**Required**): The title text. Max 150 characters.

**Schema.org property** : [Title `[title]`](https://support.google.com/merchants/answer/6324415): Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) [Structured title `[structured_title]`](https://support.google.com/merchants/answer/6324415): No |

* Use one of the title `[title]` and structured title `[structured_title]` attributes to clearly identify the product you are selling.
* For titles created using generative AI, use the structured title `[structured_title]` attribute, otherwise use the title `[title]` attribute.
* Accurately describe your product and match the title from your landing page.
* Don’t include promotional text like "free shipping", all capital letters, or gimmicky foreign characters.

For variants:

* Include distinguishing features such as color or size.

For mobile devices:

* Include “with contract” if sold with a contract.
* For the United States, include “with payment plan” if sold in installments.

For Russia:

* For books and other information products, include the age rating at the beginning of the title.

[Description `[description]`](https://support.google.com/merchants/answer/6324468) or [Structured description `[structured_description]`](https://support.google.com/merchants/answer/6324468) Your product’s description **Required** **Example** ([description `[description]`](https://support.google.com/merchants/answer/6324468)):
Made from 100% organic cotton, this classic red men’s polo has a slim fit and signature logo embroidered on the left chest. Machine wash cold; imported. Example ([structured description `[structured_description]`](https://support.google.com/merchants/answer/6324468)): `trained_algorithmic_media:"Transform your TV with the effortless power of Google Chromecast. This sleek device discreetly connects to your television, unlocking a world of wireless streaming and mirroring possibilities. From movies and TV shows to photos and presentations, cast your favorite content directly to the big screen with its integrated HDMI connector."` **Syntax**
[Description `[description]`](https://support.google.com/merchants/answer/6324468): Plain Text. Max 5000 characters [Structured description `[structured_description]`](https://support.google.com/merchants/answer/6324468): 2 sub-attributes:

* Digital source type `[digital_source_type]` (**Optional**): This sub-attribute supports 2 values:
* Default `[default]`: Specifies that the title provided using the content `[content]` sub-attribute was **not** created using generative AI.
* Trained algorithmic media `[trained_algorithmic_media]`. Specifies that the title provided using the content `[content]` sub-attribute was created using Generative AI.

If no value is specified, the Default `[default]` value is used. Content `[content]` (**Required**): The description text. Max 5000 characters **Schema.org property** : [Description `[description]`](https://support.google.com/merchants/answer/6324468): Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) [Structured description `[structured_description]`](https://support.google.com/merchants/answer/6324468): No |

* Use one of the description `[description]` and structured description `[structured_description]` attributes to accurately describe your product and match the description from your landing page.
* For descriptions created using generative AI, use the structured description `[structured_description] `attribute, otherwise use the description `[description]` attribute.
* Don’t include promotional text like "free shipping," all capital letters, or gimmicky foreign characters.
* Include only information about the product. Don’t include links to your store, sales information, details about competitors, other products, or accessories.
* Use formatting (for example, line breaks, lists, or italics) to format your description.

[Link `[link]`](https://support.google.com/merchants/answer/6324416) Your product’s landing page **Required** **Example**
`http://www.example.com/asp/sp.asp?cat=12&id=1030` **Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Use your verified domain name.
* Start with `http` or `https`.
* Use an encoded URL that complies with RFC 2396 or RFC 1738.
* Don't link to an interstitial page unless legally required.

[Image link `[image_link]`](https://support.google.com/merchants/answer/12472547) The URL of your product’s main image **Required** **Example**
`http:// www.example.com/image1.jpg` **Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) **We recently announced new image size requirements of at least 500 x 500 pixels for all product images. Enforcement of the new requirements will begin January 31, 2027.** |  For the image URL:

* Link to the main image of your product.
* Start with `http` or `https`.
* Use an encoded URL that complies with RFC 2396 or RFC 1738.
* Make sure the URL can be crawled by Google. Check your “robots.txt” file to ensure you’re not blocking “Googlebot” or “Googlebot-image” from crawling your product pages and images.

For the image:

* Accurately display the product.
* Use an accepted format: JPEG (.jpg/.jpeg), WebP (.webp), PNG (.png), non-animated GIF (.gif), BMP (.bmp), and TIFF (.tif/.tiff).
* Don't scale up an image or submit a thumbnail.
* Don't include promotional text, watermarks, or borders.
* Don't submit a placeholder or a generic image.
* All images created using generative AI must contain meta data indicating that the image was AI-generated (for example, the IPTC [`DigitalSourceType`](https://cv.iptc.org/newscodes/digitalsourcetype/)[`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia) metadata tag). Don't remove embedded metadata tags such as the IPTC `DigitalSourceType` property from images created using generative AI tools, for example [Product Studio](https://support.google.com/merchants/answer/13708167). The following IPTC NewsCodes specify the type of digital source that was used to create the image, and should be preserved:
* [`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia): The image was created using a model derived from sampled content.
* [`CompositeSynthetic`](https://cv.iptc.org/newscodes/digitalsourcetype/compositeSynthetic): The image is a composite that includes synthetic elements.
* [`AlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia): The image was created purely by an algorithm not based on any sampled training data (for example, an image created by software using a mathematical formula).

[Additional image link `[additional_image_link]`](https://support.google.com/merchants/answer/12472826) The URL of an additional image for your product **Optional** **Example**
`http://www.example.com/image1.jpg` **Syntax**
Max 2000 characters **Schema.org property** : No |

* Meet the requirements for the image link `[image_link]` attribute with these exceptions:
* The image can include product staging and show the product in use.
* Graphics or illustrations can be included.
* Submit up to 10 additional product images by including this attribute multiple times.
* All images created using generative AI must contain meta data indicating that the image was AI-generated (for example, the IPTC [`DigitalSourceType`](https://cv.iptc.org/newscodes/digitalsourcetype/)[`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia) metadata tag). Don't remove embedded metadata tags such as the IPTC `DigitalSourceType` property from images created using generative AI tools, for example [Product Studio](https://support.google.com/merchants/answer/13708167). The following IPTC NewsCodes specify the type of digital source that was used to create the image, and should be preserved:
* [`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia): The image was created using a model derived from sampled content.
* [`CompositeSynthetic`](https://cv.iptc.org/newscodes/digitalsourcetype/compositeSynthetic): The image is a composite that includes synthetic elements.
* [`AlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia): The image was created purely by an algorithm not based on any sampled training data (for example, an image created by software using a mathematical formula).

[Video Link `[video_link]`](https://support.google.com/merchants/answer/15216925) Additional link to show a video of your product. **Optional** Example
`https://example.com/video1.mpg` Syntax URL (Must start with "http://" or "https://") Up to 2000 characters Schema.org property: No |  For the video link URL:

* All video links must use a video URL, starting with “http://” or “https://”.
* Replace any special characters in video URLs with their URL-encoded equivalents. For example, replace commas with %2C. Refer to a URL encoding reference for a complete list.
* If you’re not using a YouTube URL, the URL must point directly to a raw video file. It should not be a link to a landing page that contains the video player.
* The video URL must be publicly accessible on the web. Googlebot must be able to access videos publicly without requiring logins or special permissions and with no restrictions in robots.txt.

For the video format

* Video length should be a minimum of 6 seconds and maximum of 240 seconds.
* The video file must be within the maximum file size of 500 MB.
* The aspect ratio of the video should be 9:16, 16:9, or 1:1.
* Use videos with at least a resolution of 720p (1280x720).
* The video must be in a supported file format (.MPG, .MP4, .WMV, .AVI, .MOV and .FLV .MPEG-1, .MPEGPS).

For the video content:

* Videos should not be of low resolution, blurry, or out of focus.
* Videos should not have black bars on the top, bottom, or on the sides of the video.
* Sound is optional.

Ownership and Accessibility:

* Merchants must own the content licensing rights for marketing purposes ads. No payment to creators will be made through Google. Any compensation must be handled between the brand and creator directly.

[3D model link `[virtual_model_link]`](https://support.google.com/merchants/answer/13674896) Additional link to show a 3D model of your product. **Optional** (available only in the US) **Example**
`https://www.google.com/products/xyz.glb` **Syntax** URL (Must start with "http://" or "https://") Up to 2000 characters

Schema.org property: Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* **Use a 3D model**. Your file shouldn’t exceed 15MB. Textures in the file can be up to 2K (4K isn’t supported).
* **Provide a valid URL in your product data**. The link should point to a .gltf, or .glb file.
* **Review your 3D model**. You can use [a validation tool](https://github.khronos.org/glTF-Validator/) to verify if your 3D model works properly.

[Mobile link `[mobile_link]`](https://support.google.com/merchants/answer/12472641) Your product’s mobile-optimized landing page when you have a different URL for mobile and desktop traffic **Optional** ****Example**** `http://www.m.example.com/asp/ sp.asp?cat=12 id=1030` ****Syntax****
Max 2000 alphanumeric characters ****Schema.org property** : **No |

* Meet the requirements for the link `[link]` attribute.

## Price and availability

These attributes define the price and availability for your products. This information is shown to potential customers in ads and free listings. If your products' prices and availability change often, you'll need to let us know in order to show your products. [Check out these tips for keeping your product information fresh](https://support.google.com/merchants/answer/188489)

**Attribute and format** | **Minimum requirements at a glance**
---|---
[Availability `[availability]`](https://support.google.com/merchants/answer/12472827) Your product's availability **Required** **Example**
`in_stock` **Supported values**

* In stock `[in_stock]`
* Out of stock `[out_of_stock]`
* Preorder `[preorder]`
* Backorder `[backorder]`

**Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Accurately submit the product's availability and match the availability from your landing page, checkout pages, and structured data (for example, “`in_stock`” or “`out_of_stock`” in your Schema.org markup).
* If an item is out of stock, the price must still be clearly visible on the landing page.
* Provide the [availability date `[availability_date]`](https://support.google.com/merchants/answer/6324470) attribute if you submit preorder `[preorder]` or backorder `[backorder]` as the availability value.

[Availability date `[availability_date]`](https://support.google.com/merchants/answer/6324470) The date a preordered product becomes available for delivery **Required** if product availability is set to `preorder` **Example**
(For UTC+1)
`2016-02-24T11:07+0100` **Syntax**

* Max 25 alphanumeric characters
* ISO 8601
* `YYYY-MM-DDThh:mm [+hhmm]`
* `YYYY-MM-DDThh:mmZ`

**Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Use this attribute if your product's availability is set to `preorder`. Provide a value up to one year in the future.
* The availability date should also be added to the product’s landing page and be clear to your customers (for example, “May 6, 2023”).
* If an exact date can’t be provided, you can use an estimated date (for example, “May 2023”).

[Cost of goods sold `[cost_of_goods_sold]`](https://support.google.com/merchants/answer/12471621) Your product’s description **Optional** The costs associated with the sale of a particular product as defined by the accounting convention you set up. These costs may include material, labor, freight, or other overhead expenses. By submitting the COGS for your products, you gain insights about other metrics, such as your gross margin and the amount of revenue generated by your ads and free listings. **Example**
23.00 USD **Syntax**

* ISO 4217 codes
* Use '.' rather than ',' to indicate a decimal point
* Numeric

**Schema.org property** : No |

* The currency must be in the ISO 4217 format. For example, USD for US dollars.
* The decimal point must be a period (.). For example, 10.00 USD.

[Expiration date `[expiration_date]`](https://support.google.com/merchants/answer/12471622) The date that your product should stop showing **Optional** **Example**
(For UTC+1)
`2016-07-11T11:07+0100` **Syntax**

* Max 25 alphanumeric characters
* ISO 8601
* `YYYY-MM-DDThh:mm [+hhmm]`
* `YYYY-MM-DDThh:mmZ`

**Schema.org property** : No |

* Use a date less than 30 days in the future.
* Note that a latency of several hours may occur.

[Price `[price]`](https://support.google.com/merchants/answer/12471842) Your products price **Required** **Example**
15.00 USD **Syntax**

* Numeric
* ISO 4217

**Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Accurately submit the product's price and currency, and match with the price from your landing page, structured data, and at checkout.
* Make sure that your landing page and the checkout pages include the price in the currency of the target country in a place that's straightforward to find. For ambiguous currency symbols such as “$”, use explicit symbols (for example, “S$” for Singapore Dollars, “C$” for Canadian Dollars) on your landing page.
* Ensure that the product can be purchased online for the submitted price.
* Make sure that any customer can buy the product for the submitted price, without having to sign up for a membership program (free or paid).
* If you are targeting a combination of supported and non-supported regions for loyalty programs with a free-to-join tier, [you can choose how to submit these free member prices](https://support.google.com/merchants/answer/17303094).
* Don't submit a price of 0 (a price of 0 is allowed for mobile devices sold with a contract and physical goods sold with a subscription only).
* For products sold in bulk quantities, with minimum order quantities, bundles, or multipacks.
* Submit the total price of the minimum purchasable quantity. This total price should also be prominently displayed on the landing page.
* For the US and Canada:
* Don't include any taxes, such as sales tax, Goods and Services Tax (GST), value-added tax (VAT), or import tax, in the price `[price]` attribute.
* For all other countries:
* Include value added tax (VAT) or Goods and Services Tax (GST) in the price.
* For additional options to submit price-related information, check the following attributes:
* Unit pricing measure `[unit_pricing_measure]`
* Unit pricing base measure `[unit_pricing_base_measure]`
* Sale price `[sale_price]`
* Subscription cost `[subscription_cost]`
* Installment `[installment]`
* Loyalty program `[loyalty_program]`

[Sale price `[sale_price]`](https://support.google.com/merchants/answer/12471623) Your product's sale price **Optional** **Example**
15.00 USD **Syntax**

* Numeric
* ISO 4217

**Schema.org property** : Learn more about [Merchant listing (sale pricing) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing#sale-pricing-example) on Google Search Central. |

* Meet the requirements for the price `[price]` attribute.
* Submit this attribute (sale price) in addition to the price `[price]` attribute set to the non-sale price.
* Accurately submit the product's sale price, and match the sale price with your landing page and the checkout pages.
* Don't use the sale price [sale_price]**** for loyalty prices requiring membership in a loyalty program, free or paid, in countries where the loyalty program is supported. Instead, use the [_loyalty program`[loyalty_program]`_](https://support.google.com/merchants/answer/12922446) attribute. If you are targeting a combination of supported and non-supported regions for loyalty programs with a free-to-join tier, [_you can choose how to submit these free member prices_](https://support.google.com/merchants/answer/17303094).

[Sale price effective date
`[sale_price_effective_date]`](https://support.google.com/merchants/answer/12471843) The date range during which the sale price applies **Optional** **Example**
(For UTC+1)
`2016-02-24T11:07+0100 /
2016-02-29T23:07+0100` **Syntax**

* Max 51 alphanumeric characters
* ISO 8601
* `YYYY-MM-DDThh:mm [+hhmm]`
* `YYYY-MM-DDThh:mmZ`
* Separate start date and end date with `/`

**Schema.org property** : No |

* Use together with the sale price `[sale_price]` attribute.
* If you don't submit this attribute (sale price effective date), the sale price always applies.
* Use a start date before the end date.

[Unit pricing measure
`[unit_pricing_measure]`](https://support.google.com/merchants/answer/12471624) The measure and dimension of your product as it is sold **Optional** (except when required by local laws or regulations) **Example**
`1.5kg` **Syntax**
Numerical value + unit **Supported units**

* Weight: `oz`, `lb`, `mg`, `g`, `kg`
* Volume US imperial: `floz`, `pt`, `qt`, `gal`
* Volume metric: `ml`, `cl`, `l`, `cbm`
* Length: `in`, `ft`, `yd`, `cm`, `m`
* Area: `sqft`, `sqm`
* Per unit: `ct`

**Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Use the measure or dimension of the product without packaging.
* Use a positive number.
* For variants:
* Include the same value for item group ID `[item_group_id]` and different values for unit pricing measure.

[Unit pricing base measure](https://support.google.com/merchants/answer/6324490)
`[unit_pricing_base_measure]` The product’s base measure for pricing (for example, `100ml` means the price is calculated based on a 100ml units) **Optional** (except when required by local laws or regulations) **Example**
`100g` **Syntax**
Integer + unit **Supported integers**
`1`, `10`, `100`, `2`, `4`, `8` **Supported units**

* Weight: `oz`, `lb`, `mg`, `g`, `kg`
* Volume US imperial: `floz`, `pt`, `qt`, `gal`
* Volume metric: `ml`, `cl`, `l`, `cbm`
* Length: `in`, `ft`, `yd`, `cm`, `m`
* Area: `sqft`, `sqm`
* Per unit: `ct`

**Additional supported metric integer + unit combinations**
`75cl`, `750ml`, `50kg`, `1000kg` **Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Optional when you submit the unit pricing measure `[unit_pricing_measure]` attribute.
* Use the same unit of measure for this attribute (unit pricing measure) and unit pricing base measure.
* Keep in mind that the price (or sale price, if active) is used to calculate the unit price of the product. For example, if the price `[price]` attribute is set to `3` `USD`, unit pricing measure is 150ml, and unit pricing base measure is set to 100ml, then the unit price is 2 USD / 100ml.

[Installment `[installment]`](https://support.google.com/merchants/answer/12471920) Details of an installment payment plan **Optional** **Note** :

* Not available for Display Ads.
* For Vehicle Ads: only available in certain European countries.
* For Shopping Ads and Free listings: Available in Latin America for all product categories and in certain other countries for showing wireless products and services only.

**Example** (implies a 199 EUR down payment and a "finance" credit type)
`6:30 EUR:199 EUR` **Syntax**
This attribute uses 4 sub-attributes:

* Months `[months]` (Required)
Integer, the number of installments the buyer has to pay.
* Amount `[amount]` (Required)
ISO 4217, the amount the buyer has to pay per month
* Downpayment `[downpayment]` (Optional, not available in Latin America)
ISO 4217, the amount the buyer has to pay upfront as a one time payment. Note: if you don't submit the sub-attribute, the default value is 0 or “no down payment”.
* Credit type `[credit_type]` (Optional). This sub-attribute uses the following supported values:
* Finance `[finance]`
* Lease `[lease]`

**Note** : if you don't submit the sub-attribute, the default value is finance `[finance]`. This sub-attribute is only applicable for Vehicle Ads. **Schema.org property** : No |

* Match the installment option that’s visible on your landing page.
* Don't require a loyalty card.
* Make sure the price `[price]` attribute is the total price when paid in full up-front and use the installment `[installment]` attribute to indicate an alternative payment option using installments with an optional initial down payment.

[Subscription cost `[subscription_cost]`](https://support.google.com/merchants/answer/12472643) **For mobile and wireless products** details a monthly or annual payment plan that bundles a communications service contract with a wireless product. **For Physical Goods Subscriptions** details a weekly, monthly, or annual subscription amount for a range of hard goods and physical products that can be delivered to an address. Find the [ recurring billing policy ](https://support.google.com/merchants/answer/6150006#billing) for more information. **Optional** (available only for permitted categories) **Note** :

* Mobile and wireless subscriptions are available for Shopping ads and free listings in certain countries.
* Physical Goods Subscriptions are available for Shopping ads in the United States on Google Search.

**Example** `month:12:35.00USD` **Syntax**

* Period `[period]` (Required)
The duration of a single subscription period. This sub-attribute uses the following supported values:
* Week `[week]`(Physical Goods Subscriptions only)
* Month `[month]`
* Year `[year]`
* Period length `[period_length]` (Required)
Integer, the number of subscription periods (weeks, months or years) that the buyer must pay. Must be greater than 0.
* Amount `[amount]` (Required)
* ISO 4217, the amount the buyer must pay per month. When displaying this amount, Google may round up to the nearest whole unit of local currency to save space. The provided value must still exactly match the amount as shown on your site.

**Schema.org property** : No |  **For all products:**

* Specify the offer terms of the subscription on your landing page.
* The Google Product Category `[google_product_category]` attribute must be present.

**For mobile and wireless products:**

* Include the total amount due at checkout in the price `[price]` attribute.
* When used in combination with the installment `[installment]` attribute, also include the total amount due at checkout in the downpayment `[downpayment]` sub-attribute of the installment `[installment]` attribute.
* Match the communications payment plan that you display on your landing page. The plan must be easy to find on the landing page.
* This attribute is only supported for mobile products with the following Google product category:
* Watches (ID: 201)
* Mobile Phone (ID: 267)
* Tablet Computers. (ID: 4745)
* Mobile Phone Prepaid Cards & SIM Cards (ID: 6030)
* GPS Tracking Devices (ID: 6544)

**For Physical Goods Subscriptions:**

* The`[price]` attribute must be present and provided as 0. The price value will be ignored and not shown.
* The `[sale_price] `attribute, if provided, will be ignored and not shown
* This attribute is only supported for Physical Goods Subscriptions with the following Google product category:
* Personal Care (ID: 2915)
* Health Care (ID: 491)
* Home & Garden (ID: 536)
* Pet Supplies (ID: 2)
* Toys (ID: 1253)
* Prepared Foods (ID: 5814)
* Apparel & Accessories (ID: 166)
* Coffee (ID: 1868)
* Alcoholic Beverages (ID: 499676)
* Medicine & Drugs (ID: 518)

[Loyalty program `[loyalty_program]`](https://support.google.com/merchants/answer/12922446) The loyalty program `[loyalty_program]` attribute allows setting up of member prices, loyalty points, and loyalty shipping. Optional (available for US, Australia, Brazil, Mexico, Canada, France, Germany, India, Italy, Netherlands, South Korea, Spain, and the United Kingdom, Japan ([ points program ](https://support.google.com/merchants/answer/15165113)). **Example** `my_loyalty_program:silver:10 USD::10::free_member_shipping` **Syntax**
This attribute uses 7 sub-attributes:

* Program label `[program_label]` (Optional for single tier merchants)
The loyalty program label set in your loyalty program settings in Merchant Center.
* Tier label `[tier_label]` (Optional for single tier merchants)
The tier label set in your program settings in Merchant Center, used to differentiate benefits between each tier.
* Price `[price]` (Optional) The member specific price for the program and tier. This will display alongside the non-member price to give shoppers an idea of the benefits of joining your program. This attribute should be used for free and paid memberships.
* Cashback `[cashback_for_future_use]` (optional): Reserved for future use.
* Loyalty points `[loyalty_points]` (Optional) The points that the members gain on purchasing the product on your website. This needs to be a whole number.
* Member price effective date `[member_price_effective_date]` (Optional): This sub-attribute allows merchants to specify when their member pricing benefit begins and ends.
* Shipping label `[shipping_label]` (Optional): This sub-attribute allows merchants to specify which offers are eligible for loyalty shipping. Choose your own definition for this value.

**Schema.org property** : Yes (Learn more about [Merchant listing (Member prices) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing#member-price-example) on Google Search Central) |

* Submit the loyalty program `[loyalty_program]` attribute to match the loyalty program label and tiers configured under your Merchant Center account.
* Ensure member prices are clearly accessible on your website for members, whether through a loyalty overview page, a dedicated event page, or otherwise clearly communicated to members.
* Ensure that member prices match between your product data source, landing page, and checkout.
* Member price for free and paid tiers needs to be submitted via this attribute. Submitting member price using price `[price]` or sale price `[sale_price]` is not allowed in countries where the loyalty program is supported. If you are targeting a combination of supported and non-supported regions for loyalty programs with a free-to-join tier, [you can choose how to submit these free member prices](https://support.google.com/merchants/answer/17303094).
* If you only have one tier in your loyalty program, you don’t need to submit program label `[program_label]` and tier label `[tier_label]`.
* Program label `[program_label]` and tier label `[tier_label]` are case-insensitive.

[Minimum price `[auto_pricing_min_price]`](https://support.google.com/merchants/answer/10071801) The lowest price to which a product's price can be reduced. Google uses this information for features such as sale price suggestions, automated discounts or dynamic promotions. **Optional** **Example**
`15.00 USD` **Syntax**

* Numeric
* ISO 4217

**Schema.org property** : No |

* Submit a minimum price `[auto_pricing_min_price]` attribute.
* If you are using the automated discounts or dynamic promotions feature, to specify the minimum price to which your product can be reduced.
* If you want to limit sale price suggestions to a minimum price, for example, to comply with local pricing laws or to indicate a MAP (minimum advertised price).

[Maximum retail price `[maximum_retail_price]`](https://support.google.com/merchants/answer/15972291) Your product’s price. **Optional** (available only in IN) **Example**
`15.00 INR` **Syntax**

* Numeric
* ISO 4217

|  Accurately submit the product's maximum retail price and currency, and match with the price from your landing page and at checkout. Make sure that your landing page includes the price in the currency of the target country in a place that's straightforward to find. Don't submit a price of 0 (a price of 0 is allowed for mobile devices sold with a contract).

* For the US and Canada:
* Don't include tax in the price.
* For all other countries:
* Include value added tax (VAT) or Goods and Services Tax (GST) in the price.

## Product category

You can use these attributes to organize your advertising campaigns in Google Ads and to override Google’s automatic product categorization in specific cases.

Attribute and format | Minimum requirements at a glance
---|---
[Google product category `[google_product_category]`](https://support.google.com/merchants/answer/6324436) **Optional** Google-defined product category for your product **Example**
`Apparel & Accessories > Clothing > Outerwear > Coats & Jackets` or `371` **Syntax**
Value from the Google product taxonomy

* The numerical category ID, or
* The full path of the category

**Supported values** [Google product taxonomy](https://support.google.com/merchants/answer/12472026) **Schema.org property** : No |

* Include only one category.
* Include the most relevant category.
* Include either the full path of the category or the numerical category ID, but not both. It is recommended to use the category ID.
* Include a specific category for certain products.
* Alcoholic beverages must be submitted to only certain categories.
* Mobile devices sold with contract must be submitted as:
* `Electronics > Communications > Telephony > Mobile Phones` (ID: `267`)
* `Apparel & Accessories > Jewelry > Watches` (ID: `201`)
* `Electronics > Communications > Telephony > Mobile Phone Accessories > Mobile Phone Pre-Paid Cards & SIM Cards` (ID: `6030`)
* `Electronics > GPS Tracking Devices` (ID: `6544`)
* For tablets: `Electronics > Computers > Tablet Computers` (ID: `4745`)
* Gift Cards must be submitted as `Arts & Entertainment > Party & Celebration > Gift Giving > Gift Cards & Certificates` (ID: `53`)
* Physical Goods Subscriptions must be submitted under:
* `Health & Beauty > Personal Care` (ID: `2915`)
* `Health & Beauty > Health Care` (ID: `491`)
* `Home & Garden` (ID: `536`)
* `Animals & Pet Supplies > Pet Supplies` (ID: `2`)
* `Toys & Games > Toys` (ID: `1253`)
* `Food, Beverages & Tobacco > Food Items > Prepared Foods`(ID: `5814`)
* `Apparel & Accessories` (ID: `166`)
* `Food, Beverages & Tobacco > Beverages > Coffee` (ID: `1868`)

[Product type `[product_type]`](https://support.google.com/merchants/answer/6324406) **Optional** Product category that you define for your product **Example**
`Home > Women > Dresses > Maxi Dresses` **Syntax**
Max 750 alphanumeric character **Schema.org property** : No |

* Include the full category. For example, include `Home > Women > Dresses > Maxi Dresses` instead of just Dresses
* Only the first product type value will be used to organize bidding and reporting in Google Ads Shopping campaigns

## Product identifiers

These attributes are used to provide product identifiers that define the products you're selling in the global marketplace and can help boost the performance of your ads and free listings.

Attribute and format | Minimum requirements at a glance
---|---
[Brand `[brand]`](https://support.google.com/merchants/answer/12468352) Your product’s brand name **Required** (For all new products, except movies, books, and musical recording brands) **Optional** for all other products **Example**
`Google` **Syntax**
Max 70 characters **Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Provide the brand name of the product generally recognized by consumers.
* Providing the correct brand for a product will ensure the best user experience and result in the best performance.
* Only provide **your own brand** name as the brand if you manufacture the product or if your product falls into a generic brand category.
* For example, you could submit **your** **own brand** name as the brand if you sell private-label products or customized jewelry.
* For products that truly don't have a brand (for example, a vintage dress without a label, generic electronics accessories, and other examples), leave this field empty.
* Don't submit values such as "N/A", "Generic", "No brand", or "Does not exist".
* For compatible products:
* Submit the GTIN and brand from the manufacturer who actually built the compatible product.
* Don't provide the Original Equipment Manufacturer (OEM) brand to indicate that your product is compatible with or a replica of the OEM brand's product.

[GTIN `[gtin]`](https://support.google.com/merchants/answer/12473440) Your product’s Global Trade Item Number (GTIN) **It Depends** (strongly recommended if available) **Example**
`3234567890126` **Syntax**
Max 50 numeric characters (max 14 per value - added spaces and dashes are ignored) **Supported values**

* **UPC (in North America / GTIN-12)**
12-digit number like 323456789012
8-digit UPC-E codes should be converted to 12-digit codes
* **EAN (in Europe / GTIN-13)**
13-digit number like 3001234567892
* **JAN (in Japan / GTIN-13)**
8 or 13-digit number like 49123456 or 4901234567894
* **ISBN (for books)**
10 or 13-digit number like 1455582344 or 978-1455582341. If you have both, only include the 13-digit number. ISBN-10 are deprecated and should be converted to ISBN-13
* **ITF-14 (for multipacks / GTIN-14)**
14-digit number like 10856435001702

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Exclude dashes and spaces.
* Submit only valid GTINs as defined in the official GS1 validation guide, which includes these requirements:
* The checksum digit is present and correct
* The GTIN is not restricted (GS1 prefix ranges 02, 04, 2)
* The GTIN is not a coupon (GS1 prefix ranges 98 - 99)
* Providing the correct GTIN for a product will ensure the best user experience and result in the best performance. Products with a GTIN but submitted without one may have limited visibility.
* Only provide a GTIN if you’re sure it is correct. When in doubt don’t provide this attribute (for example, do not guess or make up a value). If you submit a product with an incorrect GTIN value, your product will be disapproved.
* For compatible products:
* Submit the GTIN and brand from the manufacturer who actually built the compatible product.
* Don't provide the Original Equipment Manufacturer (OEM) brand to indicate that your product is compatible with or a replica of the OEM brand's product.
* For multipacks:
* Use the product identifiers that relates to the multipack.
* For bundles:
* Use the product identifiers for the main product in the bundle.
* If you offer customization, engraving, or other personalization of a product that's been assigned a GTIN by the manufacturer:
* Submit the GTIN and use the [bundle `[is_bundle]`](https://support.google.com/merchants/answer/12472645) attribute to let Google know that the product includes customization.

[MPN `[mpn]`](https://support.google.com/merchants/answer/12474954) Your product’s Manufacturer Part Number (MPN) **Required** (Only if your product does not have a manufacturer assigned GTIN) **Optional** for all other products **Example**
`GO12345OOGLE` **Syntax**
Max 70 alphanumeric characters **Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Only submit MPNs assigned by a manufacturer.
* Use the most specific MPN possible.
* For example, different colors of a product should have different MPNs.
* Providing the correct MPN for a product (when required) will ensure the best user experience and result in the best performance.
* Only provide an MPN if you’re sure it’s correct. When in doubt don’t provide this attribute (for example, don’t guess or make up a value).
* If you submit a product with an incorrect MPN value, your product will be disapproved.

[Identifier exists `[identifier_exists]`](https://support.google.com/merchants/answer/12472746) Use to indicate whether or not the unique product identifiers (UPIs) GTIN, MPN, and brand are available for your product. **Optional** **Example**
`no` **Supported values**

* Yes `[yes]`
Product identifiers are assigned to the new product by the manufacturer
* No `[no]`
Product lacks a brand, GTIN, or MPN (view requirements to the right). If set to `no`, still provide the UPIs you have.

**Schema.org property** : No |

* If you don't submit the attribute, the default value is `yes`.
* Your product’s category type determines which unique product identifiers (GTIN, MPN, brand) are required.
* Submit the [identifier exists](https://support.google.com/merchants/answer/12472746) attribute and set the value to `no` if:
* Your product is a media item and the GTIN is unavailable (**Note:** ISBN and SBN codes are accepted as GTINs
* Your product is an apparel (clothing) item and the brand is unavailable
* In all other categories, your product doesn’t have a GTIN, or a combination of MPN and brand
* If a product does have unique product identifiers, don’t submit this attribute with a value of “`no`” or the product may be disapproved.

## Detailed product description

These attributes are used to provide product identifiers that define the products you're selling in the global marketplace and can help ensure relevance of ad content while boosting the performance of your ads and free listings.

**Attribute and format** | **Minimum requirements at a glance**
---|---
[Adult `[adult]`](https://support.google.com/merchants/answer/12471844) Indicate a product includes sexually suggestive content **Required**(If a product contains adult content) **Example**
`yes` **Supported values**

* Yes `[yes]`
* No `[no]`

**Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Set the value of this attribute to `yes` if this individual product contains nudity or sexually suggestive content. If you don't submit the attribute, the default value is `no`. Learn more about [Adult-oriented content](https://support.google.com/merchants/answer/6150138)
* If your website is generally focused on an adult audience and contains adult-oriented content with or without nudity, indicate that in your Merchant Center settings.

Find these settings in the "Business details" tab.
[Age group `[age_group]`](https://support.google.com/merchants/answer/12472028) The demographic for which your product is intended **Required** (For all apparel products that are targeted to people in Brazil, France, Germany, Japan, the UK, and the US as well as all products with assigned age groups) **Required** for free listings for all `Apparel & Accessories` (ID: `166`) products **Optional** for all other products and target countries **Example**
`infant` **Supported values**

* Newborn `[newborn]`
0-3 months old
* Infant `[infant]`
3-12 months old
* Toddler `[toddler]`
1-5 years old
* Kids `[kids]`
5-13 years old
* Adult `[adult]`
Teens or older

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Include one value per product.
* For variants:
* Include the same value across all variants for item group ID `[item_group_id]` and the same value across all variants for item group title `[item_group_title]` and different values for age group.
* If age group is a variant-identifying property, then we recommend you provide it using both the variant option `[variant_option]` attribute and the age group `[age_group]` attribute.

[Bundle `[is_bundle]`](https://support.google.com/merchants/answer/12472645) Indicates a product is a merchant-defined custom group of different products featuring one main product **Required** (For bundles in Australia, Brazil, Czechia, France, Germany, Italy, Japan, Netherlands, Spain, Switzerland, the UK and the US) **Required** for free listings on Google if you’ve created a bundle containing a main product **Optional** for all other products and target countries **Example**
`yes` **Supported values**

* Yes `[yes]`
* No `[no]`

**Schema.org property** : No |

* Submit `yes` if you're selling a custom bundle of different products that you created, and the bundle includes a main product (for example, a camera combined with a lens and bag). If you don't submit the attribute, the default value is `no`.
* Don't use this attribute for bundles without a clear main product (for example, a gift basket containing cheese and crackers).

[Certification `[certification]`](https://support.google.com/merchants/answer/13528839) Certifications, such as energy efficiency ratings, associated with your product Available for the EU and EFTA countries and the UK **Required** for products that require certain certification information to be shown in your Shopping ads or free listings, for example due to local energy efficiency labeling regulations **Optional** for all other products **Note:** Starting April 2025, for products targeting countries in the European Union and that are required to show graphical energy efficiency class labels, use the [certification `[certification]`](https://support.google.com/merchants/answer/13528839) attribute, which references the necessary graphical energy efficiency source data through the EU [EPREL](https://eprel.ec.europa.eu/screen/home) database. The [energy efficiency class `[energy_efficiency_class]`](https://support.google.com/merchants/answer/7562785) attributes are now only available for products that target Switzerland, Norway, or the United Kingdom. **Example** `EC:EPREL:123456` **Syntax** This attribute uses the following sub-attributes:

* Authority `[certification_``authority]` Certification authority. Only "EC" or "European_Commission" supported.
* Name `[certification_``name]` Name of the certification. Only "EPREL" supported.
* Code `[certification_``code]` Code of the certification. For example, for the EPREL certificate with the link https://eprel.ec.europa.eu/screen/product
/dishwashers2019/123456 the code is 123456

**Schema.org property** : Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |  Consult EU energy efficiency regulations or any applicable local law to determine if you need to provide this attribute. This includes products covered by [EU energy labels](https://energy-efficient-products.ec.europa.eu/product-list_en), for example:

* Domestic ovens
* Electronic displays such as televisions and other external monitors
* Fridges and freezers
* Household dishwashers
* Household tumble dryers (rescaled as of July 1, 2025)
* Household washing machines and washer-dryers
* Light sources
* Range hoods
* Refrigerating appliances with a direct-sales function
* Smartphones and tablets (starting June 20, 2025)
* Solid fuel boilers
* Space heaters
* Tyres
* Ventilation units
* Water heaters

[Gender `[gender]`](https://support.google.com/merchants/answer/12471626) The gender for which your product is intended **Required** (Required for all apparel items that are targeted to people in Brazil, France, Germany, Japan, the UK, and the US as well as all gender-specific products) **Required** for free listings for all Google `Apparel & Accessories` (ID: `166`) products **Optional** for all other products and target countries **Example**
`Unisex` **Supported values**

* Male `[male]`
* Female `[female]`
* Unisex `[unisex]`

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* For some `Apparel & Accessories` (ID:`166`) categories like `Shoelaces` (ID:`1856`), this attribute is recommended instead of required since these categories aren't dependent on gender.
* For variants:
* Include the same value across all variants for item group ID `[item_group_id]` and the same value across all variants for item group title `[item_group_title]` and different values for gender.
* If gender is a variant-identifying property, then we recommend you provide it using both the variant option `[variant_option]` attribute and the gender `[gender]` attribute.

[Color `[color]`](https://support.google.com/merchants/answer/12471922) Your product’s color(s) **Required** (For all apparel products that are targeted to Brazil, France, Germany, Japan, the UK, and the US as well as all products available in different colors) **Required** for free listings for all `Apparel & Accessories` (ID: `166`) products **Optional** for all other products and target countries **Example**
Black **Syntax**
Max 100 alphanumeric characters (max 40 characters per color) **Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Don’t use a number such as "0", "2", or "4".
* Don’t use characters that aren’t alphanumeric such as "#fff000".
* Don’t use only one letter such as R. (For Chinese, Japanese, or Korean languages, you can include a single character such as 红.)
* Don’t reference the product or image such as “see image”.
* Don't combine several color names into one word, such as "RedPinkBlue"_._ Instead, separate them with a `/`, such as "Red/Pink/Blue"_._ Don’t use a value that isn’t a color, such as "multicolor", "various", "variety", "men's", "women's", or "N/A".
* If your product features multiple colors, list the primary color first.
* For variants:
* Include the same value across all variants for item group ID `[item_group_id]` and the same value across all variants for item group title `[item_group_title]` and different values for color `[color]`.
* If color is a variant-identifying property, then we recommend you provide it using both the variant option `[variant_option]` attribute and the color `[color]` attribute.

[Condition `[condition]`](https://support.google.com/merchants/answer/12471921) The condition of your product at time of sale **Required** if your product is used or refurbished **Optional** for new products **Example**
`new` **Supported values**

* New `[new]`
Brand new, original, unopened packaging
* Refurbished `[refurbished]`
Professionally restored to working order, comes with a warranty, may or may not have the original packaging
* Used `[used]`
Previously used, original packaging opened or missing

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central)
[Document link `[document_link]`](https://support.google.com/merchants/answer/17084656) The URL to a PDF document about your product **Optional** **Example**
`https://example.com/manual.pdf` **Syntax**
URL (Must start with "http://" or "https://")
Max 5 values
Up to 2000 characters **Schema.org property:** No |  For the URL:

* All document links must be a URL to a valid PDF file, starting with “http://” or “https://”.
* Replace any special characters with their URL-encoded equivalents. For example, replace commas with %2C. Refer to a URL encoding reference for a complete list.

Ownership:

* Merchants must own the content licensing rights for marketing purposes.

[Energy efficiency class `[energy_efficiency_class]`](https://support.google.com/merchants/answer/12472144) Your product’s energy efficiency class Only available for products that target Switzerland, Norway, or the United Kingdom. **Optional** (except when required by local law or regulations) **Note:** Starting April 2025, the [energy efficiency class `[energy_efficiency_class]`](https://support.google.com/merchants/answer/12472144) attributes are only available for products that target Switzerland, Norway, or the United Kingdom and are not sold in the EU. For products targeting countries in the European Union and are required to show the graphical energy efficiency class, use the [certification `[certification]`](https://support.google.com/merchants/answer/13528839) attribute, which references the necessary graphical energy efficiency source data from the EU through the [EPREL](https://eprel.ec.europa.eu/screen/home) database. **Example**
`A+` **Supported values**

* `A+++`
* `A++`
* `A+`
* `A`
* `B`
* `C`
* `D`
* `E`
* `F`
* `G`

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Include the legally required energy class.
* To be used in combination with minimum energy efficiency class `[min_energy_efficiency_class]` and maximum energy efficiency class `[max_energy_efficiency_class]` to create an energy efficiency label, for example, A+ (A+++ to G).

[Item group ID `[item_group_id]`](https://support.google.com/merchants/answer/12472646) ID for a group of products that come in different versions (variants) **Required** (Brazil, France, Germany, Japan, the United Kingdom, and the US if the product is a variant) **Required** for free listings for all product variants **Optional** for all other products and target countries **Example**
AB12345 **Syntax**
Max 50 alphanumeric characters **Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Use a unique value for each group of variants.
* Use the parent SKU where possible.
* Keep the value the same when updating your product data.
* Use only valid unicode characters.
* Specify item group title `[item_group_title]` together with item group ID****`[item_group_id] `to define a unique name for your product group.
* Specify variant option `[variant_option]` in combination with item group ID `[item_group_id]` to define all variant-identifying properties of the product, for example a t-shirt with different sizes and colors, or a laptop with different memory sizes, display sizes, processors, and graphics options.
* Specify the [ _color_` _[color]_`](https://support.google.com/merchants/answer/6324487),[ _pattern_` _[pattern]_`](https://support.google.com/merchants/answer/6324483),[ _material_` _[material]_`](https://support.google.com/merchants/answer/6324410),[ _age group_` _[age_group]_`](https://support.google.com/merchants/answer/6324463),[ _gender_` _[gender]_`](https://support.google.com/merchants/answer/6324463)[ and](https://support.google.com/merchants/answer/6324492) [_size_` _[size]_` ](https://support.google.com/merchants/answer/6324492)attributes in addition to variant option `[variant_option]` when these attributes are part of the set of variant-identifying properties.

[Item group title `[item_group_title]`](https://support.google.com/merchants/answer/17085146) A title for the parent product (product group) to which this variant belongs. Use if the product is a variant **Example**
My Brand Brilliance line Laptop **Syntax**
Text. Max 150 characters **Schema.org property** : No |

* If you provide item group ID `[item_group_id]` also provide the same item group title `[item_group_title]` for all variants that are part of the same product group.

[Material `[material]`](https://support.google.com/merchants/answer/12472145) Your product’s fabric or material **Required** (if relevant for distinguishing different products in a set of variants) **Optional** for all other products **Example**
leather **Syntax**
Max 200 characters **Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* To indicate multiple materials for a single product (not variants), add a primary material, followed by up to 2 secondary materials, separated by a `/`.
* For example, instead of "CottonPolyesterElastane", use "cotton/polyester/elastane".
* For variants:
* Include the same value across all variants for item group ID `[item_group_id]` and the same value across all variants for item group title `[item_group_title]` and different values for the material attribute.
* If material is a variant-identifying property, then we recommend you provide it using both the variant option `[variant_option]` attribute and the material `[material]` attribute.

[Minimum energy efficiency class `[min_energy_efficiency_class]`](https://support.google.com/merchants/answer/12472144) The minimum energy efficiency class in this products's category. Only available for products that target Switzerland, Norway, or the United Kingdom. **Optional** (except when required by local laws or regulations) **Note:** Starting April 2025, the [minimum energy efficiency class `[min_energy_efficiency_class]`](https://support.google.com/merchants/answer/12472144) attribute is only available for products that target Switzerland, Norway, or the United Kingdom and are not sold in the EU. For products targeting countries in the European Union and are required to show the graphical energy efficiency class, use the [certification `[certification]`](https://support.google.com/merchants/answer/13528839) attribute, which references the necessary graphical energy efficiency source data from the EU through the [EPREL](https://eprel.ec.europa.eu/screen/home) database. **Example**
`A+++` **Supported values**

* `A+++`
* `A++`
* `A`
* `B`
* `C`
* `D`
* `E`
* `F`
* `G`

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Include the legally required minimum energy efficiency class.
* To be used in combination with energy efficiency class `[energy_efficiency_class]` and maximum energy efficiency class `[max_energy_efficiency_class]` to create an energy efficiency label, for example, A+ (A+++ to D).

[Maximum energy efficiency class `[max_energy_efficiency]`](https://support.google.com/merchants/answer/12472144) The maximum energy efficiency class in this product's category. Only available for products that target Switzerland, Norway, or the United Kingdom. **Optional** (except when required by local laws or regulations) **Note:** Starting April 2025, the [maximum energy efficiency class `[max_energy_efficiency]`](https://support.google.com/merchants/answer/12472144) attribute is only available for products that target Switzerland, Norway, or the United Kingdom and are not sold in the EU. For products targeting countries in the European Union and are required to show the graphical energy efficiency class, use the [certification `[certification]`](https://support.google.com/merchants/answer/13528839) attribute, which references the necessary graphical energy efficiency source data from the EU through the [EPREL](https://eprel.ec.europa.eu/screen/home) database. **Example**
`D` **Supported values**

* `A+++`
* `A++`
* `A`
* `B`
* `C`
* `D`
* `E`
* `F`
* `G`

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Include the legally required maximum energy efficiency class.
* To be used in combination with energy efficiency class `[energy_efficiency_class]` and minimum energy efficiency class `[min_energy_efficiency_class]` to create a textual or graphical energy efficiency label, for example, A+ (G to A+++).

[Multipack `[multipack]`](https://support.google.com/merchants/answer/12472336) The number of identical products sold within a merchant-defined multipack **Required** (For multipack products in Australia, Brazil, Czechia, France, Germany, Italy, Japan, Netherlands, Spain, Switzerland, the UK and the US) **Required** for free listings on Google if you’ve created a multipack **Optional** for all other products and target countries **Example**
6 **Syntax**
Integer **Schema.org property** : No |

* Submit this attribute if you defined a custom group of identical products and are selling them as a single unit of sale (for example, you're selling 6 bars of soap together).
* Submit the number of products in your multipack. If you don't submit the attribute, the default value is `0`.
* If the product's manufacturer assembled the multipack instead of you, don't submit this attribute.

[Pattern `[pattern]`](https://support.google.com/merchants/answer/12472146) Your product’s pattern or graphic print **Required** (if relevant for distinguishing different products in a set of variants) **Optional** for all other products **Example**
striped
polka dot
paisley **Syntax**
Max 100 characters **Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) | For variants:

* Include the same value across all variants for item group ID `[item_group_id]` and the same value across all variants for item group title `[item_group_title]` and different values for the pattern attribute.
* If pattern is a variant-identifying property, then we recommend you provide it using both the variant option `[variant_option]` attribute and the pattern `[pattern]` attribute.

[Popularity rank `[popularity_rank]`](https://support.google.com/merchants/answer/17085297) Indicated the popularity of the product **Optional** **Example**
`76.5` **Syntax**
Float **Range** 0-100.0

* Decimal values are supported
* The decimal point must be a period (.)

**Schema.org property:** No |

* Use to rank the popularity of this product in your entire inventory as a percentage. The higher the number the more popular your product is.
* Note that this reflects the popularity of this product on your platform as assessed by you. It does not reflect user ratings of the product.

[Product detail `[product_detail]`](https://support.google.com/merchants/answer/9218260) Technical specifications or additional details of your product **Optional** **Example**
General:Product Type:Digital player **Syntax**
This attribute uses three sub-attributes:

* **Section name`[section_name]`**: Max 140 characters
* **Attribute name`[attribute_name]`**: Max 140 characters
* **Attribute value`[attribute_value]`**: Max 1000 characters

**Schema.org property** : No |

* Submit up to 100 product details.
* Don't add information covered in other attributes, all capital letters, gimmicky foreign characters, promotion text, or list keywords or search terms.
* Don’t add information such as price, sale price, sale dates, shipping, delivery date, other time-related information, or your company’s name.
* Only provide an attribute name and value when the value is confirmed. For example, provide “Vegetarian:False” if a food product is not vegetarian.
* Do not repeat information already provided in [_product highlight_` _[product_highlight]_`, Question and answer](https://support.google.com/merchants/answer/12471629)`[question_and_answer]`or [description `[description]`](https://support.google.com/merchants/answer/6324468).

[Product length `[product_length]`](https://support.google.com/merchants/answer/12472549) Your product's length **Optional** **Example**
`20 in` **Syntax**
Number + unit **Supported values**
`1-3000`

* Decimal values are supported

**Supported units**

* `cm`
* `in`

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Include as many of the product measurement attributes as possible.
* Use the same unit of measurement for each product dimension attribute (including product length, width, and height). Otherwise, the information won't be displayed.

[Product width `[product_width]`](https://support.google.com/merchants/answer/12472549) Your product's width **Optional** **Example**
`20 in` **Syntax**
Number + unit **Supported values**
`1-3000`

* Decimal values are supported

**Supported units**

* `cm`
* `in`

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Include as many of the product measurement attributes as possible.
* Use the same unit of measurement for each product dimension attribute (including product lengths, width, and height). Otherwise, the information won't be displayed.

[Product height `[product_height]`](https://support.google.com/merchants/answer/12472549) Your product's height **Optional** **Example**
`20 in` **Syntax**
Number + unit **Supported values**
`1-3000`

* Decimal values are supported

**Supported units**

* `cm`
* `in`

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Include as many of the product measurement attributes as possible.
* Use the same unit of measurement for each product dimension attribute (including product lengths, width, and height). Otherwise, the information won't be displayed.

[Product highlight `[product_highlight]`](https://support.google.com/merchants/answer/12471629) The most relevant highlights of your products **Optional** **Example**
Supports thousands of apps, including Netflix, YouTube, and HBO Max **Syntax**
Max 150 characters **Schema.org property** : No |

* Use between 2 and 100 product highlights.
* Describe only the product itself.
* Don't list keywords or search terms.
* Don’t include promotional text, all capital letters, or gimmicky foreign characters.
* Do not repeat information already provided in [_product detail_` _[product_detail]_`, Question and answer](https://support.google.com/merchants/answer/9218260)`[question_and_answer]`or [description `[description]`](https://support.google.com/merchants/answer/6324468).

[Product weight `[product_weight]`](https://support.google.com/merchants/answer/12472549) Your product's weight **Optional** **Example**
`3.5 lb` **Syntax**
Number + unit **Supported values**
`0-2000`

* Decimal values are supported

**Supported units**

* lb
* oz
* g
* kg

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Use the actual assembled product weight for this attribute.
* If your product comes in multiple pieces, for example, as part of a bundle, use the complete weight of all the pieces in the listing.

[_Question and answer_ `[question_and_answer]`](https://support.google.com/merchants/answer/17085211) User-, merchant-, and manufacturer-authored questions and answers about the product. **Optional** **Example (2 Q &As):**
`"Does it have a headphone jack?":"This version doesn’t have a headphone jack.", "Does it support Bluetooth?":"It has full Bluetooth 6.0 support."` **Syntax**
Group attribute. Max 30 values. Max 10000 characters total. This attribute uses 2 sub-attributes (both are required):

* **Question**`**[question]**`: Text. Max. 1000 characters.
* **Answer**`**[answer]**`: Text. Max. 1000 characters.

**Schema.org property** : No |

* Don't add information covered in other attributes, all capital letters, gimmicky foreign characters, promotion text, or list keywords or search terms.
* Don’t add information such as price, sale price, sale dates, shipping, delivery date, other time-related information, or your company’s name. Do not repeat information already provided in [_product detail_` _[product_detail]_`,](https://support.google.com/merchants/answer/9218260) [_product highlight_` _[product_highlight]_`](https://support.google.com/merchants/answer/12471629) or or [description `[description]`](https://support.google.com/merchants/answer/6324468).

[Related product `[related_product]`](https://support.google.com/merchants/answer/17085213) Specifies how other products are related to this product **Optional** **Example**
`required_part:id:AZ7A,
required_part:id:AZ7B,
accessory:gtin:811571013579` **Syntax** Group attribute. Max 30 values This attribute uses three sub-attributes (all three are required):

* **Relationship type`[relationship_type]`**. This sub-attribute supports the following values:
* **Part of set`[part_of_set]`**
Part of a set of products that are often purchased together
* **Required part`[required_part]`**
Part that is necessary for the product to function, for example a battery for a battery-operated lamp.
* **Often bought with`[often_bought_with]`**
A product that this product is often purchased together with, for example a phone case with a phone.
* **substitute`[substitute]`**
Product that this product can be substituted for, for example a cheaper alternative.
* **Different brand`[different_brand]`**
An identical product sold under a different brand, for example a cheaper house brand.
* **Accessory`[accessory]`**
An accessory to this product, for example a side table that matches the style of a couch.
* **Identifier type`[identifier_type]`.** This sub-attribute supports the following values:
* **GTIN`[gtin]`**
The identifier is a GTIN
* **ID`[id]`**
The identifier is a product ID in the feed
* **Identifier`[identifier]`**. This sub-attribute specifies the actual identifier value of the other product that is related to this product. The identifier value should match the type specified in **identifier type [`identifier_type]`.**

**Schema.org property** : No |

* If a relationship type `[relationship_type]` has multiple applicable related products, provide a separate related product[related_product] attribute for each of these related products. Do not comma-separate the identifiers as part of the identifier `[identifier]`sub-attribute.
* A product can have multiple relationship types with other products, for example, it can have one or more substitutes, one or more accessories, and one or more required parts. Provide all of these relationship types and their related products with that relationship type.

[Size `[size]`](https://support.google.com/merchants/answer/12471627) Your product’s size **Required** (Required for all apparel products in `Apparel & Accessories > Clothing` (ID:`1604`) and `Apparel & Accessories > Shoes` (ID:`187`) categories targeted to people in Brazil, France, Germany, Japan, the UK, and the US as well as all products available in different sizes) **Required** for free listings for all `Apparel & Accessories > Clothing` (ID:`1604`) and `Apparel & Accessories > Shoes` (ID:`187`) products **Optional** for all other products and target countries **Example**
XL **Syntax**
Max 100 characters **Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* For variants:
* Include the same value across all variants for item group ID `[item_group_id]` and the same value across all variants for item group title `[item_group_title]` and different values for size `[size]`.
* If size is a variant-identifying property, then we recommend you provide it using both the variant option `[variant_option]` attribute and the size `[size]` attribute.
* If sizes contain multiple dimensions, condense them into one value. For example, "16/34 Tall" is for neck size of 16 inches, sleeve length of 34 inches, and “Tall” fit
* If your item is one size fits all or one size fits most, you can use `one_size`, `OS`, `one_size fits_all`, `OSFA`, `one_size_fits_most`, or `OSFM`.
* For merchant-defined multipack products, submit the multipack quantity using the multipack `[multipack]` attribute. Do not submit the multipack quantity under the `size` attribute.

[Size type `[size_type]`](https://support.google.com/merchants/answer/12471628) Your apparel product’s cut **Optional** (Available for apparel products only) **Example**
`maternity` **Supported values**

* Regular `[regular]`
* Petite `[petite]`
* Maternity `[maternity]`
* Big `[big]`
* Tall `[tall]`
* Plus `[plus]`

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Submit up to 2 values.
* If you don't submit the attribute, the default value is `regular`.

[Size system `[size_system]`](https://support.google.com/merchants/answer/12472828) The country of the size system used by your product **Optional** (Available for apparel products only) **Example**
`US` **Supported values**

* `US`
* `UK`
* `EU`
* `DE`
* `FR`
* `JP`
* `CN`
* `IT`
* `BR`
* `MEX`
* `AU`

**Schema.org property:** Yes (Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* If you don't submit the attribute, the default value is your **target country**.

[Variant option `[variant option]`](https://support.google.com/merchants/answer/17085214) Use if the product is a variant Variant-identifying dimensions and their values **Example**
`Memory size:128 GB,Screen size:XL` **Syntax**
Group attribute. Max 30 values. Max 5000 characters total. This attribute uses two sub-attributes (both are required):

* Name`[name]`. Text. Max. 250 characters.
* Value `[value]`. Text. Max. 250 characters.

**Schema.org property** : No |

* Specify variant option [variant_option] in combination with item group ID [item_group_id] and Item group title [item_group_title]to define all variant-identifying properties of the product.
* Specify the [_color_` _[color]_`](https://support.google.com/merchants/answer/6324487),[ _pattern_` _[pattern]_`](https://support.google.com/merchants/answer/6324483),[ _material_` _[material]_`](https://support.google.com/merchants/answer/6324410),[ _age group_` _[age_group]_`](https://support.google.com/merchants/answer/6324463),[ _gender_ _[gender]_](https://support.google.com/merchants/answer/6324463)[ and](https://support.google.com/merchants/answer/6324492) [_size_ _[size]_ ](https://support.google.com/merchants/answer/6324492)attributes in addition to [variant option [variant_option]](https://support.google.com/merchants/answer/17085214) when these attributes are part of the set of variant-identifying properties.

## Shopping campaigns and other configurations

These attributes are used to control how your product data is used when you create advertising campaigns in Google Ads.

Attribute and format | Minimum requirements at a glance
---|---
[Ads redirect `[ads_redirect]`](https://support.google.com/merchants/answer/6324450) A URL used to specify additional parameters for your product page. Customers will be sent to this URL rather than the value that you submit for the link `[link]` or mobile link `[mobile_link]` attributes **Optional** **Example**
`http://www.example.com/product.html` **Syntax**
Max 2000 characters **Schema.org property** : No

|

* Submit the same registered domain as for the link `[link]`attribute (and the mobile link `[mobile_link]`attribute, if present).
* Valid registered domains include "example.com", "m-example.com", "example.co.uk", "example.com.ai", and "bar.tokyo.jp".
* URLs submitted with invalid domains, such as "example.zz" or "example.comic", will not be accepted. For more details on valid registered domains, check ads redirect.

[Custom label 0-4 `[custom_label_0-4]`](https://support.google.com/merchants/answer/6324473) Label that you assign to a product to help organize bidding and reporting in Shopping campaigns **Optional** **Example**
Seasonal
Clearance
Holiday
Sale
Price range **Syntax**
Max 100 characters **Schema.org property** : No |

* Use a value that you'll recognize in your Shopping campaign. The value won't be shown to customers who view your ads and free listings.
* Submit up to 5 custom labels per product by including this attribute multiple times:
* `custom_label_0`
* `custom_label_1`
* `custom_label_2`
* `custom_label_3`
* `custom_label_4`
* Use only 1,000 unique values for each custom label across your Merchant Center account.

[Promotion ID `[promotion_id]`](https://support.google.com/merchants/answer/7050148) An identifier that allows you to match products to promotions **Optional** (Required for promotions in Australia, France, Germany, India, the UK and the US) **Example**
ABC123 **Syntax**
Max 50 characters **Schema.org property** : No |

* Use a unique and case sensitive ID without spaces or symbols (for example, %, !).
* To map specific promotions to specific products, submit the same promotion ID in your product data and promotion data.
* Submit up to 10 promotion IDs for one product by including this attribute multiple times.

[Lifestyle image link `[lifestyle_image_link]`](https://support.google.com/merchants/answer/9103186) Attribute used to include the URL for a lifestyle image for your product Only available for browsy surfaces **Optional** **Example** `https://www.example.com/image1.jpg` **Syntax** Max 2000 characters **Schema.org property** : No |

* Use a URL that points to an image in a supported file format
* Start with `http` or `https` and comply with RFC 3986
* Replace any symbols or spaces with URL encoded entities
* Make sure Google can crawl your URL
* All images created using generative AI must contain meta data indicating that the image was AI-generated (for example, the IPTC [`DigitalSourceType`](https://cv.iptc.org/newscodes/digitalsourcetype/)[`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia) metadata tag). Don't remove embedded metadata tags such as the IPTC `DigitalSourceType` property from images created using generative AI tools, for example [Product Studio](https://support.google.com/merchants/answer/13708167). The following IPTC NewsCodes specify the type of digital source that was used to create the image, and should be preserved:
* [`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia): The image was created using a model derived from sampled content.
* [`CompositeSynthetic`](https://cv.iptc.org/newscodes/digitalsourcetype/compositeSynthetic): The image is a composite that includes synthetic elements.
* [`AlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia): The image was created purely by an algorithm not based on any sampled training data (for example, an image created by software using a mathematical formula).

[Short title `[short_title]`](https://support.google.com/merchants/answer/11551083) Short product name Only available for Demand Gen Ads, including YouTube, Gmail, Maps, Discover app, Google Display Network, and Google Video Partners. Learn more [About Demand Gen campaigns](https://support.google.com/google-ads/answer/13695777). **Optional** **Example**
Running shoes **Syntax**
Plain text. Max 150 characters (Recommended: 5–65 characters) **Schema.org property** : No |

* `[short_title]` can optionally be provided for Demand Gen campaigns. `[title]` must still be provided.

## Marketplaces

These attributes are used to control how your product data is used if you are a marketplace and are using a multi-seller account.

**Attributes and format** | **Requirements at a glance**
---|---
[External seller ID `[external_seller_id]`](https://support.google.com/merchants/answer/11537846) **Required** for multi-seller account Used by a marketplace to externally identify a seller. (For example, on a website) **Example** SellerPublicName1991 **Syntax** 1 - 50 characters **Schema.org property** : No |

* Use a unique value for each seller.
* Keep the ID the same when updating your data
* Use only valid characters. Avoid invalid characters like control, function, or private area characters
* Use the same ID for the same seller across countries or languages

## Destinations

These attributes can be used to control the different locations where your content can appear. For example, you could use this attribute if you want a product to appear in a dynamic remarketing campaign, but not in a Shopping ads campaign.

Attributes and format | Requirements at a glance
---|---
[Excluded destination `[excluded_destination]`](https://support.google.com/merchants/answer/12472337) A setting that you can use to exclude a product from participating in a specific type of advertising campaign ******Optional** **Example**
`Shopping_ads` **Supported values**

* `Shopping_ads`
* `Buy_on_Google_listings`
* `Display_ads`
* `Local_inventory_ads`
* `Free_listings`
* `Free_local_listings`
* `YouTube_Shopping`

Some values only available for the classic version of Merchant Center. **Schema.org property** : No

|
[Included destination `[included_destination]`](https://support.google.com/merchants/answer/12472550) A setting that you can use to include a product in a specific type of advertising campaign ******Optional** **Example**
`Shopping_ads` **Supported values**

* Shopping_ads
* Buy_on_Google_listings
* Display_ads
* Local_inventory_ads
* Free_listings
* Free_local_listings
* YouTube_Shopping

Some values only available for the classic version of Merchant Center. **Schema.org property** : No |
[Excluded countries for Shopping ads](https://support.google.com/merchants/answer/9837523) `[shopping_ads_excluded_country]` A setting that allows you to exclude countries where your products are advertised on Shopping ads ** Optional** Only available for Shopping ads **Example**
DE **Syntax**
2 characters. Must be an [ISO_3166-1_alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. **Schema.org property** : No |
[Pause `[pause]`](https://support.google.com/merchants/answer/12472831) A setting you can use to pause and quickly reactivate a product for all ads (including Shopping ads, Display ads, and local inventory ads). A product can be paused for up to 14 days. If a product is paused for more than 14 days it will be disapproved. To re-approve, remove the attribute. ******Optional** **Example**
`ads` **Supported values**
`ads` **Schema.org property** : No |

## Shipping and returns

These attributes can be used together with the account shipping settings and return settings to help you provide accurate shipping and return costs. People who are shopping online rely on shipping costs and speeds, as well as return policies, to help them make choices about what to buy, so it's important to take the time to submit quality information.

Attribute and format | Minimum requirements at a glance
---|---
[Shipping `[shipping]`](https://support.google.com/merchants/answer/12471847) Your product's shipping cost, shipping speeds, and the locations your product ships to **It depends** **Shipping costs are required** for Shopping ads and free listings for the following countries: Australia, Austria, Belgium, Canada, Czechia, France, Germany, India, Ireland, Israel, Italy, New Zealand, Japan, the Netherlands, Poland, Romania, South Korea, Spain, Switzerland, the UK, and the US You may also be required to provide shipping costs based on local laws or regulations. **Optional** (to specify additional countries your product ships to or destinations where shipping costs are not required) **Supported prices**
0–1000 USD ([check for other currencies](https://support.google.com/merchants/answer/6324484#format)) **Example**
`US:CA:Overnight:16.00 USD:1:1:2:3` **Syntax**
This attribute uses the following sub-attributes:

* **Country`[country]` (Required)**
* ISO 3166 country code
* **Region`[region]`(Optional)**
* **Postal code`[postal_code]`(Optional)**
* **Location ID`[location_id]` (Optional)**
* **Location group name`[location_group_name]` (Optional)**
* **Service`[service]` (Optional)**
* Service class or shipping speed
* [Price](https://support.google.com/merchants/answer/12471842)**`[price]` (Optional)**
* Fixed shipping cost, including VAT if required
* [Minimum handling time](https://support.google.com/merchants/answer/12472338)**`[min_handling_time]` **and****[maximum handling time](https://support.google.com/merchants/answer/12472338)**`[max_handling_time]` (Optional)**
* To specify handling time
* **Minimum transit time` [min_transit_time]`** and **maximum transit time`[max_transit_time]`** (Optional)
* To specify transit time
* [Shipping transit business days](https://support.google.com/merchants/answer/16072858)**`[shipping_transit_business_days]`(Optional)**
* [Shipping handling business days](https://support.google.com/merchants/answer/16072859)**`[shipping_handling_business_days]`(Optional)**
* [Loyalty program label](https://support.google.com/merchants/answer/12922446)**`[loyalty_program_label]`(Optional)**
* [Loyalty program tier label](https://support.google.com/merchants/answer/12922446)**`[loyalty_tier_label]`(Optional)**

**Schema.org property:**`Yes `(Learn more about [Merchant listing (Product, Offer) structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) on Google Search Central) |

* Use this setting when shipping costs for your product are not defined in your Merchant Center account or when you need to override shipping costs or speeds defined in your Merchant Center account.
* **Don't include government- imposed fees** such as import duties, recycling fees, copyright fees, or state-specific retail delivery fees in the shipping cost.
* **Include all additional fees that you charge as a merchant if they are not included in the product price**. Include the charges that aren't directly related to shipping but relevant for the purchase during checkout. For example, service, processing, activation, and handling fees that you charge.

[Carrier shipping `[carrier_shipping]`](https://support.google.com/merchants/answer/15449142) Shipping services you use when delivering a product. **Optional** **Example** `US:80302:USPS_MEDIA_MAIL:1:3:2:5` **Syntax** This attribute uses the following sub-attributes:

* **Country`[country]` (Required)**
* ISO 3166 country code
* **Region`[region]` (Optional)**
* **Postal code`[postal_code]` (Optional)**
* **Origin Postal code`[origin_postal_code] `(Required)**
* The domestic ZIP postal code. For the UK use outward code.
* **Location ID`[location_id]` (Optional)**
* **Shipping Price (Required)**
Choose only one from below:
* **Manual Price`[flat_price]`**
* **Carrier price`[carrier_price]`**
* **Flat price adjustment`[carrier_price_flat_adjustment]`** and **Percentage price adjustment`[carrier_price_percentage_adjustment]` (Optional)**
* To specify carrier rate discounts or added fees
* **Minimum handling time`[min_handling_time]`** and **maximum handling time`[max_handling_time]` (Optional)**
* To specify handling time
* **Shipping transit time (Optional)**
Choose only from from below:
* **Fixed transit time**
* **Minimum transit time`[fixed_min_transit_time]`, maximum transit time `[fixed_max_transit_time]`(Optional)**
* **Carrier transit time`[carrier_transit_time]`**
* **Loyalty program label`[loyalty_program_label]`(Optional)**
* **Loyalty program tier label`[loyalty_tier_label]`(Optional)**

**Schema.org property** : No |

* **For general delivery details, use account settings in Merchant Center**. Use this setting only as a last resort.
* **Don't include government- imposed fees** such as import duties, recycling fees, copyright fees, or state-specific retail delivery fees in the shipping cost.

[Handling cutoff time `[handling_cutoff_time]`](https://support.google.com/merchants/answer/16543665) Daily deadline for processing online orders **Optional** **Example** `US:16.00 USD` **Syntax** This attribute uses the following sub-attributes:

* **Country`[country]` (Optional)**: [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country code
* **Cutoff time`[cutoff_time]` (Required)**: time of day by which an order must be placed to be processed on that same business day.
* **Cutoff timezone`[cutoff_timezone]` (Optional)**: Timezone for the specified cutoff_time in [IANA Timezone](https://en.wikipedia.org/wiki/Tz_database) format (for example, “America/Los_Angeles”. If not provided, the system will default to the timezone of the shipping destination.
* **Disable delivery after cutoff`[disable_delivery_after_cutoff]`(Optional)**: This boolean setting controls the visibility of delivery options after the cutoff time has passed. Default=False

**Schema.org property** : No |

* Use 24-hour format for cutoff time. Specify "23:59" for no cutoff time.
* Specify Cutoff timezone` [cutoff_timezone]` for a cutoff time based on the shipping origin's timezone (for example, a warehouse). If not specified the user's (destination) timezone is used.

[Minimum order value `[minimum_order_value]`](https://support.google.com/merchants/answer/16989009) Minimum spend required for an order including this product. **Optional** **Example** `US:16.00 USD` **Syntax** This attribute uses the following sub-attributes:

* **Country**`**[country]**`**(Required)**
* [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country code
* **Service**`**[service]**`**(Optional)**
* Service class or shipping speed
* **Surface**`**[surface]**`**(Optional)**
* The destinations the specified minimum order value applies to. Either Online `[online]`, Local `[local]`, or online plus local `[online_local]`. Default is online plus local `[online_local]`.
* **Price**`**[price]**`**(Required)**
* The minimum spend required to place an order

**Schema.org property** : No |

* The minimum order value currency must be the same as the offer's price currency.
* The currency must be in the ISO 4217 format. For example, USD for US dollars.
* The decimal point must be a period (.). For example, 10.00 USD.

[Shipping label` [shipping_label]`](https://support.google.com/merchants/answer/6324504) Label that you assign to a product to help assign correct shipping times and transit costs in Merchant Center account settings **Optional** **Example** perishable **Syntax** Max 100 characters **Schema.org property** : No |

* Use a value that you'll recognize in your account shipping settings. The value won't be shown to customers. Examples:
* Sameday
* Oversize
* Only FedEx

[Shipping weight `[shipping_weight]`](https://support.google.com/merchants/answer/12472551) The weight of the product used to calculate the shipping cost **Optional** (Required for carrier-calculated rates in your account shipping settings) **Supported weights**

* 0–2000 lbs for imperial
* 0–1000 kgs for metric

**Example**
`3 kg` **Syntax**
Number + unit **Supported units**

* `lb`
* `oz`
* `g`
* `kg`

**Schema.org property** : No |

* Submit this value if you set up account shipping settings for carrier-calculated rates or weight-based shipping services

[Shipping length `[shipping_length]`](https://support.google.com/merchants/answer/12472832) The length of the product used to calculate the shipping cost by dimensional weight **Optional** (Required for carrier-calculated rates in your account shipping settings) **Example**
`20 in` **Syntax**
Number + unit **Supported values**

* 1 - 150 for inches
* 1 - 400 for cm

**Supported units**

* `in`
* `cm`

**Schema.org property** : No |

* Submit this value if you set up account shipping settings for carrier-calculated rates.
* If you don't provide shipping dimension attributes while using carrier-calculated rates, Google won't be able to calculate rates based on the dimensional weight of the product. If that's the case, we'll just calculate the rates based on the value you provided in the shipping weight `[shipping_weight]` attribute.
* If you submit this attribute, submit all shipping dimension attributes:
* Shipping length `[shipping_length]`
* Shipping width `[shipping_width]`
* Shipping height `[shipping_height]`
* Use the same unit for all shipping dimension attributes that apply to a single product.
* Google doesn't automatically calculate additional shipping cost for oversized products. If your package would be considered large or oversized by your carrier, you should use the shipping `[shipping]` attribute to set shipping cost for an individual product.

[Shipping width `[shipping_width]`](https://support.google.com/merchants/answer/12472832) The width of the product used to calculate the shipping cost by dimensional weight **Optional** (Required for carrier-calculated rates in your account shipping settings) **Example**
`20 in` **Syntax**
Number + unit **Supported values**

* 1 - 150 for inches
* 1 - 400 for cm

**Supported units**

* `in`
* `cm`

**Schema.org property** : No |

* Meet the requirements for the shipping length `[shipping_length]` attribute.

[Shipping height `[shipping_height]`](https://support.google.com/merchants/answer/12472832) The height of the product used to calculate the shipping cost by dimensional weight **Optional** (Required for carrier-calculated rates in your account shipping settings) **Example**
`20 in` **Syntax**
Number + unit **Supported values**

* 1 - 150 for inches
* 1 - 400 for cm

**Supported units**

* `in`
* `cm`

**Schema.org property** : No |

* Meet the requirements for the shipping length `[shipping_length]` attribute.

[Ships from country `[ships_from_country]`](https://support.google.com/merchants/answer/9837936) A setting that allows you to provide the country from which your product will typically ship ******Optional** **Example**
`DE` **Syntax**
2 characters. Must be an [ISO_3166-1_alpha-2 ](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)country code. **Schema.org property** : No |

* Provide only the country from which you typically ship this product.

[Maximum handling time `[max_handling_time]`](https://support.google.com/merchants/answer/12472338) The longest amount of time between when an order is placed for a product and when the product ships **Optional** **Example**
3 **Syntax**
Integer, greater than or equal to 0 **Schema.org property** : No |

* Submit this attribute if you want to display the overall time it takes for a product to arrive at its destination.
* Submit the number of business days (as configured in Merchant Center).
* For products ready to be shipped the same day, submit 0.
* For submitting a time range submit maximum handling time `[max_handling_time]` in combination with minimum handling time `[min_handling_time]`.

[Minimum handling time `[min_handling_time]`](https://support.google.com/merchants/answer/12472338) The shortest amount of time between when an order is placed for a product and when the product ships **Optional** **Example**
1 **Syntax**
Integer, greater than or equal to 0 **Schema.org property** : No |

* Meet the requirements for the maximum handling time `[max_handling_time]` attribute.

[Shipping transit business days `[shipping_transit_business_days]`](https://support.google.com/merchants/answer/16072858) Days of the week that your product is in transit when shipped to a customer. **Optional** **Example** `Mon-Fri;Sun
US:Mon-Sat` **Syntax** This attribute uses the following sub-attributes:

* **Country`[country]` (Required)**
* ISO 3166 country code
* **Business Days`[business_days]` (Required)**
* Semicolon separated attributes for each day of the week, or a range of days separated by a dash.

**Supported values**

* `M, Mon, Monday` for Monday
* `T, Tue, Tuesday` for Tuesday
* `W, Wed, Wednesday` for Wednesday
* `R, Thu, Thursday` for Thursday
* `F, Fri, Friday` for Friday
* `S, Sat, Saturday` for Saturday
* `U, Sun, Sunday` for Sunday

**Schema.org property** : No |

* Submit this attribute with Shipping handling days `[shipping_handling_business_days]` to calculate shipment delivery.
* Defaults to `Mon-Sat` when not filled.
Configuration applies to all countries when not specified.
* A maximum of **10** **transit business day** configurations are allowed.

[Shipping handling business days `[shipping_handling_business_days]`](https://support.google.com/merchants/answer/16072859) Days of the week that your business is operational. Use this to help calculate handling time. **Optional** **Example** `Mon-Fri;U
US:Tue-Fri;Sun` **Syntax** Semicolon separated attributes for each day of the week, or a range of days separated by a dash. **Supported values**

* `M, Mon, Monday` for Monday
* `T, Tue, Tuesday` for Tuesday
* `W, Wed, Wednesday` for Wednesday
* `R, Thu, Thursday` for Thursday
* `F, Fri, Friday` for Friday
* `S, Sat, Saturday` for Saturday
* `U, Sun, Sunday` for Sunday

**Schema.org property** : No |

* Submit this attribute if you want to customize your business operational days for handling time.
* Defaults to `Mon-Sat` when not filled.
* A maximum of **10** **handling business days** configurations are allowed.

[Free shipping threshold `[free_shipping_threshold]`](https://support.google.com/merchants/answer/14768922) Order cost above which shipping is free. **Optional** **Example**
`US:16.00 USD` **Syntax**
This attribute uses the following sub-attributes:

* **Country`[country]` (Required)**
* ISO 3166 country code
* **Price threshold`[price_threshold]` (Required)**
* Order cost above which shipping is free.

**Schema.org property** : No |

* The free shipping threshold currency must be the same as the offer's price currency.
* The currency must be in the ISO 4217 format. For example, USD for US dollars.
* The decimal point must be a period (.). For example, 10.00 USD.

[Return`[return]`](https://support.google.com/merchants/answer/17081382) Used to configure your return policy at the product level. **Optional** (Strongly recommended for each product) **Example** `US:90:IN_STORE:BY_MAIL:REFUND:EXCHANGE` **Syntax** This attribute uses the following sub-attributes:

* **Country`[country]` (Required)**
* [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country code
* **Item condition`[item_condition]` (Required)**: The condition of the product that’s accepted for return.
* Supported values:
* `NEW`
* `LIKE_NEW`
* `USED`
* `DEFECTIVE_ONLY`
* **Window days`[window_days]` (Optional, Required if `[window_type]` is `FINITE_RETURN_WINDOW`)**
* **Window type`[window_type]` (Optional)**
* Supported values:
* `FINITE_RETURN_WINDOW`
* `NO_RETURNS`
* `LIFETIME`
* Default is `FINITE_RETURN_WINDOW`.
* **Method`[method]` (Required)**
* Supported values:
* `BY_MAIL`
* `IN_STORE`
* `AT_A_KIOSK`
* `DROP_OFF_LOCATION`
* **Outcome`[outcome]` (Optional)**: The outcome of the return.
* Supported values:
* `REFUND`
* `EXCHANGE`
* `STORE_CREDIT`
* **Shipping fee`[shipping_fee]` (Required)**
* Default return shipping cost is 0.
* **Shipping fee type`[shipping_fee_type]` (Optional, Required** **if** **`[shipping_fee]` is submitted)**
* Supported values:
* `DEDUCTED_FROM_REFUND`
* `CUSTOMER_RESPONSIBILITY`
* **Restocking fee`[restocking_fee]` (Optional)**
* Submit only one of `restocking_fee `or `restocking_percentage_fee`.
* Default restocking fee is 0.
* **Restocking percentage fee`[restocking_percentage_fee]` (Optional)**: Submit only one of `restocking_fee` or `restocking_percentage_fee`.
* **Policy url`[policy_url]` (Optional)**: The url linking the exact return policy for the product.

**Schema.org property** : No |

* Submit this attribute if you want to override any account-level return policies for a single product.
* Products with offer-level returns don’t require account-level return policies.
* Name the sub-attributes you are using in the attribute header.
* Return`[return]`attributes without an attribute header will assume the default attribute format:
1. Country`[country]`
2. Window days`[window_days]`
3. Item condition`[item_condition]`
4. Method`[method]`
5. Shipping fee `[shipping_fee]`
* Use the Return`[return]`attribute sparingly. Use account-level return policies instead to manage the majority of your product catalog.

[Return policy label `[return_policy_label]`](https://support.google.com/merchants/answer/9445425)

Label used to assign the correct return policy as defined in Merchant Center account settings **Optional** **Example** `**my_label**` **Syntax** Max 100 characters **Schema.org property** : No |

* Apply this attribute for products with non-standard return policies
* If no value is provided, the default return policy you configured will be applied
* Use a value that you assigned in your account return policies. The value won't be shown to customers. **Examples:**
* Unlimited
* Oversize
* FinalSale