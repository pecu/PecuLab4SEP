import React from "react";

export function MintVisit({ mintVisit }) {
  return (
    <div>
      <h4>MintVisit</h4>
      <form
        onSubmit={(event) => {
          // This function just calls the transferTokens callback with the
          // form's data.
          event.preventDefault();

          const formData = new FormData(event.target);
          const to = formData.get("to");
          const tokenURI = formData.get("tokenURI");

          if (to && tokenURI) {
            mintVisit(to, tokenURI);
          }
        }}
      >
        <div className="form-group">
          <label>Visit NFT Mint address</label>
          <input className="form-control" type="text" name="to" required />
          <label>Visit NFT Mint URI</label>
          <input className="form-control" type="text" name="tokenURI"
          value="https://ipfs.io/ipfs/QmR1ikAX3GKo1Gqnw1XqKR896RycHVEfz7WkrGdaKq7B8g?filename=PID0004.json" required />
        </div>
        <div className="form-group">
          <input className="btn btn-primary" type="submit" value="MintVisit" />
        </div>
      </form>
    </div>
  );
}
