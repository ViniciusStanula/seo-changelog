Get the latest announcements on new features, bug fixes, and release updates.

## May 2026

## May 2026

What's new:

- A new Merchant API MCP service (alpha version) with authorized access to your Merchant Center data and insights with a focus on read-only is now available as a new agentic tool for Merchant API.
- New conversational attributes are now available under - `ProductAttributes`in the Products sub-API.- These attributes include:
- A full set of attributes specifically for vehicle ads has been added in the Products sub-API.
- Notifications on product status changes for Universal Commerce Protocol (UCP) checkout are now available in the Notifications API through the reporting context value - `FREE_LISTINGS_UCP_CHECKOUT`.
- Merchant API Agent Skills is the new agentic tool within the Code Assist Toolkit. The new - `mapi-developer-assistant`skill, built on the open Agent Skills standard, provides intelligent and contextual assistance. It brings domain-specific expertise, automated workflows, and enhanced efficiency within AI tools like Antigravity CLI and IDEs to accelerate your integration.
- A new YouTube sub-API v1alpha version is available for managing YouTube Affiliate Program contracts.
- Added support to manage YouTube Shopping Affiliate and product reviews programs in the Accounts sub-API.
- A new data source is available for product promotions at the advanced account level.

What's changed:

- The Merchant API v1beta version discontinued. All API calls must now be directed to the `v1`or`v1alpha`versions. For migration steps, see Migrate from v1beta to v1.
- More frequent attribute-level updates to `price`and`availability`are now available through the`patch`method in the Products sub-API. This feature enables higher data freshness by allowing you to update these specific attributes with lower latency. Currently, this is only available to allowlisted merchants. To learn more or request access, contact your Google representative.

What's coming:

- Analytics for agentic performance with UCP in the Reports API.

## January 2026

## January 2026

What's new:

- A new reporting context value, - `FREE_LISTINGS_UCP_CHECKOUT`to understand the product eligibility status for UCP (Universal Commerce Protocol) checkout in the Reports sub-API.
- YouTube Shopping Affiliates performance reporting introduced in v1alpha within the Reports sub-API.
- Added support for - `ErrorInfo`messages to provide machine-readable metadata for erroneous API calls. This is accompanied by a new guide on error handling and a full list of error messages.

What's changed:

- Added `InventoryLoyaltyProgram`to the local inventory service to allow users to have consolidated control over loyalty features, such as discounts, cashback for future purchases, and loyalty points.

What's coming:

- **Discontinuation of Merchant API v1beta on February 28, 2026**. Direct all API calls to v1 and v1alpha versions, respectively, before the v1beta sunset deadline.
- Ability to enable and disable the Product Reviews program through the Reviews API v1alpha, which streamlines the process of submission and management of product reviews.

## November 2025

## November 2025

What's new:

- New insights for YouTube Shopping affiliate analytics (v1alpha), in Reports sub-API to retrieve analytics about creators, content, and products featured on YouTube. It provides parity to the existing reports available in Google Merchant Center (GMC).
- An upgraded API diagnostics tool to support the migration to Merchant API(v1).
- Added a new field `product_filters`, to the Accounts sub-API to let merchants to share only a subset of their feed with Google Ads accounts, based on some conditional filters on the attributes of the merchant's products. This feature is only accessible to a limited number of merchants.
- Added support for the creation of standalone accounts for sellers on ecommerce platforms.
- Added two new methods, `accounts.limits.get`and`accounts.limits.list`to query account limits in the Quota API.

What's changed:

- Support for automatic detection and internal decoding of base64url-encoded product IDs is now available across all methods that use product IDs.

What's coming:

- New insights for YouTube Shopping affiliate analytics (v1alpha), in Reports sub-API to retrieve analytics about creators, content, and products featured on YouTube. It provides parity to the existing reports available in Google Merchant Center (GMC).
- Discontinuation of v1beta version in Merchant API on February 28, 2026. All API calls must be directed to v1 and v1alpha versions respectively, before the v1beta sunset deadline. For more information, see Merchant API versioning and sunset policy.

## September 2025

## September 2025

What's new:

- The first Model Context Protocol (MCP) service
for Merchant API is available.
- The new MCP service integrates authoritative Google API documentation into your Integrated Development Environment (IDE) coding assistant to accelerate your Merchant API integration and improve the accuracy of your migration workflows.

- A new method, `getAccountForGcpRegistration`in the Accounts sub-API to retrieve the merchant account that's registered with Google Cloud.

What's changed:

- New methods for Regions management
in the Accounts sub-API.
- The introduction of three new methods, `batchCreate`,`batchDelete`, and`batchUpdate`to enable call batching for`create`,`update`, and`delete`operations for Regions in the Accounts sub-API to facilitate region management and mitigate the limitations of`one-region-per-request`calls.

- The introduction of three new methods,
- A new carrier-based shipping configuration is available in the Products sub-API to specify shipping attributes on product level.

What's coming:

- New reports for YouTube Shopping affiliate program analytics, such as v1alpha in Reports sub-API to retrieve analytics about creators, content, and products featured on YouTube that provides parity with reports available in Google Merchant Center.
- Enabling more frequent product updates for availability and price attributes.
- Easier analysis of API errors with enriched ErrorInfo and metadata.

## July 2025

## July 2025

What's new:

- Merchant API (v1) - The official successor of the Content API for Shopping is now generally available. - This means that going forward, there will only be v1alpha and v1 sub-APIs within Merchant API, with most v1beta versions graduating to v1. Stay tuned for more information.
- New resources are available. - Image resource in Product Studio API (alpha) leverages genAI to generate new product backgrounds, remove image background, and upscale image resolution.
- Checkout on Merchant in Accounts sub-API provides the ability to create, update, delete, and get your checkout settings.
- Online Return Policy in Accounts sub-API has been migrated, with user functionality remaining unchanged. Small technical improvements, such as outdated fields and renaming existing fields have been removed for consistency.
- `AccountIdAlias`in the AccountRelationship resource in Accounts sub-API uses a user-defined alias instead of your internal ID (account ID). This makes it easier to manage complex account structures, such as use of user-defined alias for your marketplace instead of your internal ID.

- Access to Merchant API is now available for Apps Script users.
- A new - `AggregateProductStatuses`method is now available in the Issue resolution API to query amalgamated statistics about product statuses.

What's changed:

- Ability to create standalone accounts for storebuilders and CSSs. Previously merchant accounts were created under a single advanced account.
- Click potential rankings in the - `productView`table under the Reports sub-API. Now, ranking of products based on- `clickPotential`is normalized to values between 1 and 1000. Products with low- `clickPotentialRank`still have the highest- `click potential`among the merchant's products that fulfill the search query conditions.

What's coming:

- Access through Model Context Protocol (MCP) server (v1alpha).

## May 2025

## May 2025

What's new:

- We launched two new sub-APIs.
- Order tracking supports business order tracking history to provide precise and accurate shipping estimates to customers. Its signals also enable enhanced listings with free and fast shipping.
- Issue resolution provides access to diagnostic content and support actions in the same way as it's available in the Merchant Center UI.

- New resources are available in the Accounts sub-API.
- `OmnichannelSettings`manages the account configuration for omnichannel serving, such as Free Local Listings (FLL) and Local Inventory Ads (LIA).
- `LfpProviders`connects to Local Feeds Partnership (LFP) partners for inventory data.
- `GbpAccounts`connects to Google Business Profile account for local store data.
- `OnlineReturnPolicy`provides the ability to create, delete and update your online policies.

- A new method is available in the Products sub-API.
- `ProductsUpdate`lets you update individual products without the need to provide all the fields required for- `ProductInput`.

What's changed:

- The maximum `pageSize`increased from 250 to 1000 rows per API call.
- A delay that existed for product insertion, promotions, product reviews, and
merchant reviews after `DataSources`creation is fixed.

What's coming:

- Deprecation and future removal of the channel field for `DataSources`and products.
- Launch of an updated definition for `clickPotentialRank`in the`productView`table under the Reports sub-API:- Ranking of products based on `clickPotential`is normalized to values between 1 and 1000.
- Products with low `clickPotentialRank`still have the highest click potential among the merchant's products that fulfill the search query conditions. This is a non-breaking change that might be launched on July 1, 2025.

- Ranking of products based on
- The `AccountIdAlias`in the`AccountRelationship`resource, makes it possible to better manage complex account structures. For example, marketplaces use a user-defined alias instead of the merchant's internal ID, such as account ID.

## April 2025

What's new:

- We launched a new sub-API.
- Product Studio (ALPHA) leverages genAI to generate and optimize product titles and descriptions.

- New resources are available in the Accounts sub-API.
- `AutomaticImprovements`manages the opt-in to three automatic update features provided by the Google Merchant Center platform:
- `AccountService`and- `AccountRelationship`resources manage relationships and establish services to service providers.

- We launched three fields for
`AutomatedDiscounts`in the Products sub-API to retrieve real-time prices for products opted into Google Automated Discounts (GAD).

What's changed:

- We now support destinations, known as marketing methods in Merchant Center for the Data Sources sub-API.
- We made multiple adjustments to the resource and recommend to review the Accounts release notes for more details.
- The fields `taxes`and`tax_category`in the Products sub-API are deprecated in line with the deprecation of`accounttax`in the Content API.

What's coming:

- We've taken your feedback into consideration and are working on several areas to improve API developer documentation.
- Stay tuned and check back in more frequently, and feel free to give us more feedback.