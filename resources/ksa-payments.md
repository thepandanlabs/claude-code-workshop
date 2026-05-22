# KSA Payment Notes

**For attendees in Saudi Arabia subscribing to Claude Pro.**

Anthropic officially supports Saudi Arabia for both Claude.ai and the API. No VPN, no workaround. But card declines do happen, and they have predictable causes.

## What works

- **International Visa or Mastercard.** Credit or debit. The most reliable route.
- **Mada cards co-badged on Visa or Mastercard rails.** Most newer Mada cards are dual-badged — check the back of the card. If it has a Visa or Mastercard logo alongside the Mada logo, it can be used for international online purchases.
- **Apple Pay through the Claude iOS app.** In-app purchases go through Apple's billing rails rather than Anthropic's Stripe checkout. If your card is fussy on Stripe but fine on Apple Pay, this is the workaround.
- **STC Pay-funded virtual cards.** Generate a one-time virtual Visa or Mastercard from STC Pay and use that.

## What does not work

- PayPal, Venmo, and other third-party processors — Anthropic doesn't accept them on web checkout.
- Mada-only cards (no Visa/Mastercard co-badge). These are domestic-rail-only and won't work internationally.
- Cards from banks that have international online payments disabled by default. See below.

## The most common KSA-specific decline cause

**Your bank has international online payments disabled.** Many KSA-issued cards ship with this setting off by default. Symptoms: the Claude Pro checkout returns a generic "card declined" error, and your bank's app shows no transaction attempt at all.

Fix it in your bank's mobile app:

- **Al Rajhi:** Cards → Manage Card → Internet Purchases → toggle on.
- **SNB:** Cards → Card Controls → Online Purchases (International) → enable.
- **Riyad Bank:** Card Services → International Transactions → enable.
- **Alinma:** Card Controls → e-Commerce International → enable.
- **stc pay:** Already enabled by default for the virtual cards.

Each bank's exact menu wording shifts over time. The setting you want says something like "international", "online", or "e-commerce" purchases.

After enabling, retry the Claude Pro checkout. The toggle takes effect immediately.

## What about currency

Anthropic bills in USD. Your bank converts at the daily rate plus its FX margin (typically 1.5–2.5%). The \$20/month Pro plan ends up roughly SAR 75–80 on your statement, varying with the rate.

## What about VAT and invoices

Anthropic's checkout supports adding a VAT number if you're subscribing on behalf of a registered Saudi entity. The invoice you get back is in USD and is valid for ZATCA expense submission. If your finance team needs a specific format, raise a ticket via `support.claude.com` after subscribing — Anthropic support is generally responsive on this within a couple of working days.

## Still stuck

If you've tried two cards and Apple Pay and nothing works, the fallback is to ask a colleague outside KSA to subscribe and add you to a workspace — though for this workshop you'll specifically want your own account so your usage doesn't conflict with theirs. Message the facilitator before the workshop and we'll figure out a fallback together.

[← Back to home](index.html)
