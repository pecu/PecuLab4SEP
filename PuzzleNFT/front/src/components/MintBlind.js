import React from "react";

export function MintBlind({ mintblind }) {
  return (
    <div>
      <h4>MintBlind</h4>
      <form
        onSubmit={(event) => {
          // This function just calls the transferTokens callback with the
          // form's data.
          event.preventDefault();

          const formData = new FormData(event.target);
          const nft_id = formData.get("nft_id");
          const to = formData.get("to");

          if (nft_id && to) {
            mintblind(nft_id, to);
          }
        }}
      >
        <div className="form-group">
          <label>Blind NFT Mint address</label>
          <input className="form-control" type="text" name="to" required />
          <label>Blind NFT Mint Id</label>
          <input className="form-control" type="text" name="nft_id" required />
        </div>
        <div className="form-group">
          <input className="btn btn-primary" type="submit" value="MintBlind" />
        </div>
      </form>
    </div>
  );
}
