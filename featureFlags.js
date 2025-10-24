// featureFlags.js
export const isGpt5Enabled = () => process.env.FEATURE_GPT5_ENABLED === 'true';

// usage
if (isGpt5Enabled()) {
  // serve GPT-5 to all clients
} else {
  // fallback
}